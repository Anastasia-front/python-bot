import os

from log_functions import print_directory, print_filename, print_subdirectory


def recursive_directory_walk(directory, original_directory=None):
    # Set the original directory to the provided directory if not specified
    if original_directory is None:
        original_directory = directory

    if len(str(directory)) == len(str(original_directory)):
        print_directory(directory.name)
        subdirectories_processed = (
            False  # Flag to check if any subdirectories were processed
        )

        for root, dirs, files in os.walk(directory):
            # Process files in the current directory
            for file in files:
                print_filename(file)

            if dirs:
                print_subdirectory(dirs)
                subdirectories_processed = True

                # Recursive call for each subdirectory
                for subdir in dirs:
                    subdir_path = os.path.join(root, subdir)
                    recursive_directory_walk(subdir_path, original_directory)

        # Print "It's over" if no subdirectories were processed
        if not subdirectories_processed:
            print("It's over")
