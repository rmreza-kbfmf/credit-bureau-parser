# p_parser/pipeline.py

import glob
import os
import json
import xmltodict
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm

from credit_bureau_parser.registry import get_feature_set, get_processors
from credit_bureau_parser.utils.parser_utils import (
    remove_namespace,
    replace_nil_true,
    get_nested_dict,
    wrap_dicts_as_lists,
)


class FileProcessor:
    """
    Callable worker class for processing a single file
    """

    def __init__(
        self,
        processors,
        output_format,
        data_type,
        base_output_dir,
        feature_set,
    ):
        self.processors = processors
        self.output_format = output_format
        self.data_type = data_type
        self.base_output_dir = base_output_dir
        self.feature_set = feature_set

    def __call__(self, filename: str):
        try:
            # ---- Load file ----
            if self.data_type == "xml":
                with open(filename, "r", encoding="utf-8") as f:
                    root = xmltodict.parse(
                        f.read(),
                        attr_prefix="",
                        dict_constructor=dict,
                    )
            else:
                with open(filename, "r", encoding="utf-8") as f:
                    root = json.load(f)

            # ---- Normalize ----
            root = remove_namespace(root)
            root = replace_nil_true(root)
            root = wrap_dicts_as_lists(root)
            root = get_nested_dict(root, self.feature_set.ROOT)

            # ---- Run processors ----
            for ProcessorClass in self.processors:
                processor = ProcessorClass(
                    root=root,
                    filename=filename,
                    folder_path=self.base_output_dir,
                    data_type=self.data_type,
                )
                processor.process(output_format=self.output_format)

            return {
                "filename": filename,
                "status": "success",
            }

        except Exception as e:
            return {
                "filename": filename,
                "status": "failed",
                "error": str(e),
            }

class FileProcessingPipeline:
    def __init__(
        self,
        root_base: str,
        data_type: str,
        output_format: str,
        bureau_name: str = "pefindo",
        processor_set: str = "default",
        use_multiprocessing: bool = False,
        use_tqdm: bool = False

    ):
        self.data_type = data_type
        self.output_format = output_format
        self.bureau_name = bureau_name
        self.processor_set = processor_set
        self.use_multiprocessing = use_multiprocessing
        self.use_tqdm = use_tqdm

        self.feature_set = get_feature_set(self.bureau_name, self.data_type)
        self.processors = get_processors(self.processor_set)

        self.root_base = Path(root_base).resolve()

        self.input_dir = self.root_base / "input" / self.bureau_name / self.data_type
        self.output_dir = self.root_base / "output" / self.bureau_name / self.data_type

        if not self.input_dir.exists():
            raise FileNotFoundError(f"Input dir not found: {self.input_dir}")

        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.file_list = sorted(
            self.input_dir.glob(f"*.{self.data_type}"),
            key=os.path.getmtime,
            reverse=True,
        )

    def run(self):
        worker = FileProcessor(
            processors=self.processors,
            output_format=self.output_format,
            data_type=self.data_type,
            base_output_dir=str(self.output_dir),
            feature_set=self.feature_set,
        )

        if self.use_multiprocessing:
            self._run_parallel(worker)
        else:
            self._run_sequential(worker,self.use_tqdm)

    # -------------------------------
    # 🧵 Parallel (LOCAL ONLY)
    # -------------------------------
    def _run_parallel(self, worker):
        success, failed = 0, 0
        failed_files = []

        with ProcessPoolExecutor() as executor:
            future_to_filename = {
                executor.submit(worker, str(filename)): str(filename)
                for filename in self.file_list
            }

            for future in tqdm(
                as_completed(future_to_filename),
                total=len(future_to_filename),
                desc=f"Processing {self.data_type.upper()} files",
            ):
                filename = future_to_filename[future]

                try:
                    result = future.result()
                    if result["status"] == "success":
                        success += 1
                    else:
                        failed += 1
                        failed_files.append(
                            (filename, result.get("error", "Unknown error"))
                        )
                except Exception as e:
                    failed += 1
                    failed_files.append((filename, str(e)))

        self._print_summary(success, failed, failed_files)

    # -------------------------------
    # 🧠 Sequential (AIRFLOW SAFE)
    # -------------------------------
    def _run_sequential(self, worker, use_tqdm: bool = False):
        success, failed = 0, 0
        failed_files = []

        iterable = self.file_list

        if use_tqdm:
            iterable = tqdm(
                self.file_list,
                desc=f"Processing {self.data_type.upper()} files",
                unit="file",
            )        

        for filename in iterable:
            try:
                result = worker(str(filename))
                if result["status"] == "success":
                    success += 1
                else:
                    failed += 1
                    failed_files.append(
                        (filename, result.get("error", "Unknown error"))
                    )
            except Exception as e:
                failed += 1
                failed_files.append((str(filename), str(e)))

        self._print_summary(success, failed, failed_files)

    # -------------------------------
    # 📊 Summary
    # -------------------------------
    @staticmethod
    def _print_summary(success, failed, failed_files):
        print(f"\n✅ Success: {success}")
        print(f"❌ Failed: {failed}")

        if failed_files:
            print("\n❌ Failed files:")
            for f, err in failed_files:
                print(f" - {f}: {err}")