# 11. Write a python program to rename a file to “renamed_by_python.txt”.

from pathlib import Path

folder = Path(__file__).resolve().parent
source_file = folder / "file_to_rename.txt"
target_file = folder / "renamed_by_python.txt"

source_file.write_text("This file was renamed by Python.", encoding="utf-8")

if target_file.exists():
    target_file.unlink()

source_file.rename(target_file)

