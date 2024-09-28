import os

# Function to print the contents of a directory
def print_directory_contents(path):
    try:
        # List all files and directories in the given path
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access {path}.")

# Example usage: printing contents of the current directory
print_directory_contents(".")
