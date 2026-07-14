# 3. Write a program to generate multiplication tables from 2 to 20 and write them to different
# files. Place these files in a folder for a 13-year-old.

from pathlib import Path

folder = Path(__file__).resolve().parent / "for_13_year_old"
folder.mkdir(exist_ok=True)


def generate_table(n):
    lines = [f"Multiplication Table of {n}"]
    for i in range(1, 11):
        lines.append(f"{n} X {i} = {n * i}")

    file_path = folder / f"table_{n}.txt"
    file_path.write_text("\n".join(lines), encoding="utf-8")


for number in range(2, 21):
    generate_table(number)
