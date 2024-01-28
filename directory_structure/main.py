import sys
from pathlib import Path

from walk_directory import recursive_directory_walk


def directory_structure(path):
    path = Path(path)
    if path.exists():
        recursive_directory_walk(path)
    else:
        print('No such directory')


try:
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
        directory_structure(directory_path)
    else:
        print("Please provide a directory path as a command-line argument.")
except Exception as error:
    print(f"Error - {error}")

# Example of use:

# If you execute the script and pass it the absolute path 
# to the directory as a parameter.

# python executed_file /path/to/your/directory // 
# python3 directory_structure/main.py /Users/Anastasia/Desktop/python_bot/phone_book

