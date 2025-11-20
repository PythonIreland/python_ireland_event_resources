import os
import pytest
from pathlib import Path
from typing import List


def count_columns(file_name: Path) -> None:
    first_line: bool            = True
    expected_column_count: int  = 0

    with open(file_name, mode="r", encoding="utf-8") as my_file:
        for line in my_file:
            
            # All lines must match the header of the file:
            if first_line:
                first_line = False
                expected_column_count = len(line.split(","))

            assert expected_column_count == len(line.split(","))


def test_column_count() -> None:
    """
    This test will ensure all lines have the same number of columns as the header.

    For every .csv file:
        Count the number of lines in the first line - the file header.
        Ensure all lines match this count.
    """
    # TODO: Hard coded path for now:
    cwd: Path               = Path.cwd()
    csv_realpath: Path      = Path(f"{cwd}/pycons/2025/resources.csv")
    print(f"Testing file: {csv_realpath}")
    count_columns(csv_realpath)

