import networkx as nx
import os
import platform

def open_file_with_default_program(filename):
    """ Opens the specified file using the system's default program for the file type. """
    try:
        if platform.system() == 'Windows':
            os.startfile(filename)
        elif platform.system() == 'Darwin':  # macOS
            os.system(f'open "{filename}"')
        else:  # Linux and other systems
            os.system(f'xdg-open "{filename}"')
    except Exception as e:
        print(f"Failed to open {filename}: {e}")

# Example usage
# Make sure to replace 'example.txt' with the path of the file you want to open
filename = 'example.txt'
open_file_with_default_program(filename)
