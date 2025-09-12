import networkx as nx

def open_file_with_default_program(filename):
    import os
    os.startfile(filename)

# Usage
open_file_with_default_program('example.txt')
