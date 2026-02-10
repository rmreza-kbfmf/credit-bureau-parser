# credit-bureau-parser

This package is about credit bureau parser, which translate document data into tabular data

Currently compatible with Credit Bureau:
* **Pefindo** 
  * XML versions **5.82** and **5.31**.
  * JSON version **1.0.3_12**.

## Requirements

* Minimal Python `3.11.9`
* Libraries listed in `requirements.txt`

---

## Tags Covered
| Section                          | Progress XML | Progress JSON | Notes / Reason                                                                 |
| -------------------------------- | ------------ | ------------- | ------------------------------------------------------------------------------ |
| CIP                              | ✅            | ✅             |                                                                                |
| CIP Reason                       | ✅            | ❌             | Too hard to implement due to different format with XML                         |
| CIQ                              | ✅            | ❌             | No more data in JSON                                                          |
| Collaterals                      | ✅            | ✅             |                                                                                |
| ContractOverview                 | ✅            | ✅             |                                                                                |
| Contracts                        | ✅            | ✅             |                                                                                |
| ContractSummary                  | ✅            | ✅             |                                                                                |
| ContractPaymentCalendar          | ✅            | ✅             |                                                                                |
| CurrentRelations                 | ✅            | ❌             | No more data in JSON                                                          |
| CurrentRelations Related Party   | ✅            | ❌             |                                                                                |
| Dashboard                        | ✅            | ❌             | Redundant data with others and some no longer exist in JSON                   |
| Disputes                         | ✅            | ❌             | No more data in JSON                                                          |
| Individual                       | ✅            | ✅             |                                                                                |
| Inquiries                        | ✅            | ✅             |                                                                                |
| Involvements                     | ✅            | ❌             | No more data in JSON                                                          |
| OtherLiabilities                 | ✅            | ❌             | No more data in JSON                                                          |
| Parameters                       | ✅            | ✅             | No more data in JSON howver needed as jon table                                                         |
| ReportInfo                       | ✅            | ❌             | No more data in JSON                                                          |
| Securities                       | ✅            | ❌             | No more data in JSON, moved to *Fasilitas* with code **F03**                  |
| SubjectInfoHistory               | ✅            | ✅             |                                                                                |



❌ : Meaning we're not using it anymore <br>
✅ : Meaning we're still using it although some field not exists
---

## Features

The main features of this parser are:

**Parser**: Converts Type Data (XML or JSON) files to `.csv` and optionally `.parquet` format.

---

## How to Use

### Parser

1. Create a virtual environment based on the python versionand install dependencies from `requirements.txt`.

```bash

# Set venv by using specific python version
python3.11.9 -m venv .venv

# activate the venv
.venv\Scripts\activate

# install the package for latest version
pip install git+https://github.com/rmreza-kbfmf/credit-bureau-parser.git

# install the package for debugging
pip install -e .
```

2. Place `.XML` or `.JSON` files inside `{root-base}/input/{bureau-name}/{output-format}/`.

   * For example, if the root folder located in `./opt/airflow/resources` with bureau name `pefindo` and file type is `xml` then use: `./opt/airflow/resources/input/pefindo/xml/`
   * For example, if the root folder located in `./opt/airflow/resources` with bureau name `clik` and file type is `json` then use: `./opt/airflow/resources/input/clik/json/`



3. Run the parser using:

```bash
# Example: parse JSON files and save output as CSV
python -m credit_bureau_parser.main --data-type json --output-format csv

# Example: parse XML files and save output as Parquet
python -m credit_bureau_parser.main --data-type xml --output-format parquet
```
python src\credit_bureau_parser\testing_compare_result.py baseline\output\pefindo\json resources\output\pefindo\json

4. Arguments explanation:

| Argument          | Description                               | Example                     |
| ----------------- | ----------------------------------------- | --------------------------- |
| `--data-type`     | Format of data to parse (`json` or `xml`) | `--data-type json`          |
| `--root-base`   | Path to the folder containing input files | `--folder-path opt/airflow/` |
| `--output-format` | Output file format (`csv` or `parquet`)   | `--output-format parquet`   |
| `--bureau-name` | bureau name, default is `pefindo`   | `--bureau-name pefindo`   |
| `--processor-set` | Processing all or certain file, default is all file   | `--processor-set default`   |
| `--use-multiprocessing` | Argument to enable multiprocessing, not work in airflow, default is single processing   | `--use-multiprocessing`   |
| `--use-tqdm` | Argument to enable tqdm, not work in airflow, default is using tqdm   | `--use-tqdm`   |


5. Output location: 

Output files for each processor will be saved under the `{root-base}/output/{bureau-name}/{output-format}/` folder (e.g. `./opt/airflow/resources/output/pefindo/xml/`).
If the output folder does not exist, it will be created automatically before saving.
