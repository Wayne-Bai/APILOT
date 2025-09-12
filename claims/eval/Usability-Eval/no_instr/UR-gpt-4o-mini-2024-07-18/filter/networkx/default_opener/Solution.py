import networkx as nx
import os
import platform

def open_file_with_default_program(filename):
    if platform.system() == 'Windows':
        os.startfile(filename)
    elif platform.system() == 'Darwin':  # macOS
        os.system(f'open "{filename}"')
    else:  # Linux and other systems
        os.system(f'xdg-open "{filename}"')

# Example usage
file_to_open = 'example.txt'
open_file_with_default_program(file_to_open)
