import networkx as nx
import os

def open_file_with_system(filename):
    # Check if the file exists
    if os.path.exists(filename):
        # Open the file with system's default program
        os.startfile(filename)
    else:
        print("File does not exist.")

# Example usage
filename = 'example.txt'
open_file_with_system(filename)
