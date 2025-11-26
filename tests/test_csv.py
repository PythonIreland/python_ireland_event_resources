# pylint: disable=line-too-long
"""
    This test will perform a sanity check on the edits made to the resources.csv located in each pycon folder:
        pycon/2025/resources.csv
"""
from pathlib import Path
from typing import List
from csv import reader as csv_reader


def count_columns(file_name: Path) -> None:
    """
    Count all of the comma separated rows of the header and compare that to each line in the file.
    """
    first_line: bool            = True
    expected_column_count: int  = 0

    with open(file_name, mode="r", encoding="utf-8") as my_file:
        my_csv = csv_reader(my_file)
        for line in my_csv:
            # All lines must match the header of the file:
            if first_line:
                first_line = False
                expected_column_count = len(line)

            assert expected_column_count == len(line)

def test_column_count() -> None:
    """
    This test will ensure all lines have the same number of columns as the header.

    For every .csv file:
        Count the number of lines in the first line - the file header.
        Ensure all lines match this count.
    """
    cwd: Path               = Path.cwd()
    basedir: Path           = Path(f"{cwd}/pycons/")
    csv_files: List[Path]   = list(basedir.rglob("*/resources.csv"))
    print("\n")
    for cur_path in csv_files:
        print(f"Testing file: {cur_path}")
        count_columns(cur_path)
