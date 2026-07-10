# 4. Write a python program to print the contents of a directory using the os module. Search
# online for the function which does that.

import os


def print_directory_contents(path="."):
    """Print the names of files and directories in the given path."""
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Directory not found: {path}")
        return
    except PermissionError:
        print(f"Permission denied: {path}")
        return

    print(f"Contents of directory: {os.path.abspath(path)}")
    for entry in entries:
        print(entry)


if __name__ == "__main__":
    directory = input("Enter directory path (leave blank for current directory): ").strip() or "."
    print_directory_contents(directory)

