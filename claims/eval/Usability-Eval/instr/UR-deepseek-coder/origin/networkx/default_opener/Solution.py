import networkx as nx
import subprocess

def open_file_with_default_program(filename):
    try:
        subprocess.run(['start', filename], check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error opening file: {e}")

# Example usage
filename = "example.txt"
open_file_with_default_program(filename)
