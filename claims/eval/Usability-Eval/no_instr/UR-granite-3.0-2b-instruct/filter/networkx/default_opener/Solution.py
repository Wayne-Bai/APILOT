import networkx as nx
from os import startfile

def open_file(filename):
    G = nx.Graph()
    G.add_node(filename)
    startfile(filename)

# Example usage:
open_file("example.txt")
