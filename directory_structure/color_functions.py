from colorama import Fore


def print_directory(path):
    print(f"\n {Fore.GREEN} directory {Fore.RESET} {path} \n")


def print_subdirectory(path):
    print(f"\n      {Fore.CYAN} subdirectory {Fore.RESET} {path} \n")


def print_filename(path):
    print(f"            {Fore.MAGENTA} file {Fore.RESET} {path}")
