import datetime
from multiprocessing import Queue

from credit_bureau_parser.args import parse_args
from credit_bureau_parser.pipeline import FileProcessingPipeline
from credit_bureau_parser.registry import get_processors
from credit_bureau_parser.utils.logger_utils import setup_logger_listener


def run(
    data_type=None,
    output_format=None,
    processor_set=None,
    bureau_name=None,
    root_base=None,
    use_multiprocessing=None,
    use_tqdm=False
):
    """
    Unified entry point for:
    - CLI
    - Airflow
    - Direct Python calls
    """

    args = parse_args()
    data_type = data_type or args.data_type
    output_format = output_format or args.output_format
    processor_set = processor_set or args.processor_set
    bureau_name = bureau_name or args.bureau_name
    root_base = root_base or args.root_base   
    use_tqdm = use_tqdm or args.use_tqdm 

    # 🔥 multiprocessing resolution (explicit > CLI > default)
    use_multiprocessing = (
        use_multiprocessing
        if use_multiprocessing is not None
        else args.use_multiprocessing
    )
    log_queue = Queue()
    log_filename = datetime.datetime.now().strftime("logs/processor_log_%Y-%m-%d.log")
    listener = setup_logger_listener(log_queue, log_filename)

    try:
        pipeline = FileProcessingPipeline(
            root_base=root_base,
            data_type=data_type,
            output_format=output_format,
            bureau_name=bureau_name,
            processor_set=processor_set,
            use_multiprocessing=use_multiprocessing,
            use_tqdm=use_tqdm
        )

        pipeline.run()

    except Exception as e:
        print(f"ERROR in MAIN : {e}")

    finally:
        listener.stop()


if __name__ == "__main__":
    run()