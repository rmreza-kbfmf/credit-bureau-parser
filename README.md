# credit-bureau-parser

Brand new parser. 
Currently compatible with Credit Bureau:
* **Pefindo** 
  * XML versions **5.82** and **5.31**.
  * JSON version **1.0.3_12**.

## Requirements

* Minimal Python `3.11.9`
* Libraries listed in `requirements.txt`
* A `db_config.json` file (for SQL credentials) in the following format:

```json
{
    "server": "",
    "database": "",
    "username": "",
    "password": "",
    "driver": ""
}
```

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



❌ : Meaning we're not using it anymore
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

# install the requirements
pip install -r requirements.txt
```

2. Place `.XML` or `.JSON` files inside `dir/input/{typefile}/`.

   * For example, if the desired file is xml then use: `dir/input/xml/`
   * For example, if the desired file is json then use: `dir/input/json/`

3. Run the parser using:

```bash
# Example: parse JSON files and save output as CSV
python main.py --data-type json --output-format csv

# Example: parse XML files and save output as Parquet
python main.py --data-type xml --output-format parquet
```

4. Arguments explanation:

| Argument          | Description                               | Example                     |
| ----------------- | ----------------------------------------- | --------------------------- |
| `--data-type`     | Format of data to parse (`json` or `xml`) | `--data-type json`          |
| `--folder-path`   | Path to the folder containing input files | `--folder-path dir/input/` |
| `--output-format` | Output file format (`csv` or `parquet`)   | `--output-format parquet`   |

however `--folder-path` can be null as the default value is `dir/input/`

5. Output location: 

Output files for each processor will be saved under the `dir/output/{typefile}` folder (e.g. `dir/output/json/CIP.csv`).
If the output folder does not exist, it will be created automatically before saving.


## Notes

* ⚠️ The `.parquet` output is still experimental and currently slower, as it first generates `.csv` before converting to `.parquet`.
* 🧩 Next Step : Create pipeline for formatting data and ingestion

---
