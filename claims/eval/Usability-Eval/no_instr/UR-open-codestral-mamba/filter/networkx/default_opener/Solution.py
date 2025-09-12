import subprocess
import os
import webbrowser
import networkx as nx

def open_file_with_default_program(filepath):
    """Opens a file using the user's default program."""
    # Get the default application for the file extension
    ext = os.path.splitext(filepath)[-1].lower()
    with os.popen(f'xdg-mime query default {ext}') as p:
        default_app = p.read().strip()

    # Use the default application to open the file
    subprocess.call([default_app, filepath])

# Create a NetworkX graph
G = nx.Graph()

# Add some nodes and edges to the graph
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_edge("A", "B")
G.add_edge("B", "C")

# Save the graph to a file
nx.write_gml(G, "graph.gml")

# Open the file using the user's default program
open_file_with_default_program("graph.gml")
