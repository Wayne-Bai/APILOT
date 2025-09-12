import networkx as nx
import os
import subprocess

# Create a new graph
G = nx.Graph()

# Add nodes and edges
G.add_node("file1")
G.add_node("file2")
G.add_node("file3")
G.add_edge("file1", "file2")
G.add_edge("file2", "file3")
G.add_edge("file1", "file3")

def open_file(filename):
    """
    Opens filename using system’s default program.
    
    Args:
    filename (str): Name of the file to be opened.
    """
    if os.name == 'nt':  # for windows
        os.startfile(filename)  
    else:  # for macOs/linux variants
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])  

def main():
    # Node to be opened
    filename = "example.txt"

    # Ensure the node/file exists
    if G.has_node(filename):
        open_file(filename)
    else:
        print("File not found in graph")

if __name__ == "__main__":
    import sys
    main()
