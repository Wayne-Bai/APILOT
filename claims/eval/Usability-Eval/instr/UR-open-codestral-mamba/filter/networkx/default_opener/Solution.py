import os
import networkx as nx

# Open the filename using system's default program
def open_file(file_name):
    if os.name == 'nt':
            os.system(f"start {file_name}")
    elif os.name == 'posix':
            os.system(f"open {file_name}")

# Create a graph
G = nx.Graph()
G.add_node("YourFile.txt")

# Open the file using the system default application
open_file("YourFile.txt")
