import os
import subprocess

def open_file(file_path):
    # Get the default application for the file type
    default_application = os.getenv('DEFAULT_APPLICATION', '')

    if default_application:
        # If a default application is set, use it to open the file
        subprocess.call([default_application, file_path])
    else:
        # If no default application is set, use the built-in file open function
        with open(file_path, 'r'):
            print(file_path)

# Example usage:
open_file('example.txt')
