import networkx as nx
import webbrowser
import os

# Create a new directed graph
G = nx.DiGraph()

# Add nodes to the graph
G.add_node("open_file")

# Add edges to the graph with their respective node names (command names) and descriptions
actions = {
    "open_file": {"action": "O", "command": "start", "description": "Open a file", "args": {"cmd": "start"}},
}

# Iterate over each node and add the corresponding action to the graph
for node, attributes in actions.items():
    G.add_edge("start", node, label=attributes["description"])

# Read command names from the graph
command_nodes = [node for node in G.nodes() if G.out_degree(node) > 0]

# Create the Node-Label-Group
nlg = nx.multipartite_layout(G, align="horizontal")

# Define a function to draw the graph
def draw_graph(G):
    pos = nlg
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightblue', edge_color='gray')
    labels = nx.get_edge_attributes(G,'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
    
# Import required modules
import matplotlib.pyplot as plt

# Open the file with its default application
for node in command_nodes:
    if node == "open_file":
        # Get the cmd argument for the open_file action
        for edge in G.edges():
            if edge[1] == node:
                # Get the directory path for the current open_file action
                description = edge[2]['label']
                # Print the description
                print(f"Opening file: {description}")
                # Open the file
                webbrowser.open(f'C:\\path\\to\\file')
                # Open the default application for the file type
                os.system('explorer /select,"C:\\path\\to\\file"')

# Draw the graph
draw_graph(G)
