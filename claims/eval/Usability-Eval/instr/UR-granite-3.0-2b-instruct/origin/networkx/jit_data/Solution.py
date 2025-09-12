import networkx as nx
import json

# Create a graph
G = nx.Graph()

# Add nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")

# Add edges
G.add_edge("A", "B")
G.add_edge("B", "C")

# Function to return data in JIT JSON format
def get_graph_data():
    data = {
        "nodes": [node for node in G.nodes()],
        "edges": [tuple(edge) for edge in G.edges()],
    }
    return json.dumps(data, indent=4)

# Print the graph data
print(get_graph_data())
