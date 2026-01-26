import argparse
import os
import datetime


def parse_args():
    """
    Parse CLI arguments for p-parser
    """
    parser = argparse.ArgumentParser(description="Run Credit Bureau parsing pipeline")

    parser.add_argument(
        "--bureau-name",
        default="pefindo",
        help="Credit Bureau Name"
    )

    parser.add_argument(
        "--data-type",
        choices=["xml", "json"],
        default="xml",
        help="Input data type"
    )

    parser.add_argument(
        "--output-format",
        choices=["csv", "parquet"],
        default="csv",
        help="Output file format"
    )

    parser.add_argument(
        "--root-base",
        default="resources",
        help="Base directory containing input folders (xml/json)"
    )



    parser.add_argument(
        "--processor-set",
        default="default",
        help="Processor set name (from config)"
    )

    # 🔑 AIRFLOW-SAFE
    args, _ = parser.parse_known_args()
    
    return args