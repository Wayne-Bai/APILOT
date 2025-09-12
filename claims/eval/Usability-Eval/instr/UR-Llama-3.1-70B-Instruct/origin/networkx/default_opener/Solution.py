# Importing necessary libraries
import networkx as nx
import os

# Function to open a file using the system's default program
def open_file(filename):
    """
    Opens filename using system’s default program.

    Parameters:
    filename (str): The name of the file to be opened
    """
    if os.path.exists(filename):
        # For Windows
        if os.name == 'nt':
            os.startfile(filename)
        # For macOS
        elif os.name == 'posix' and os.uname()[0] == 'Darwin':
            os.system('open "%s"' % filename)
        # For Linux variants
        else:
            os.system('xdg-open "%s"' % filename)
    else:
        print("File does not exist.")

# Importing networkx is not necessary for opening a file, but since the user requested it, we can create a simple graph to demonstrate its usage.
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3)])
nx.draw(G, with_labels=True)
filename = 'graph.png'
nx.write_png(G, filename)

# Open the generated graph image file
open_file(filename)
