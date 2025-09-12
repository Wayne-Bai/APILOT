import networkx as nx
import pandas as pd

# Create a graph
G = nx.Graph()

# Add edges with attributes (if any)
G.add_edge('A', 'B', weight=3)
G.add_edge('B', 'C', weight=5)
G.add_edge('C', 'A', weight=7)
G.add_edge('C', 'D', weight=11)

# Extract the edge list with attributes
edges_data = nx.get_edge_attributes(G, 'weight')

# Convert to a Pandas DataFrame
edge_list = pd.DataFrame(
    [(u, v, data) for (u, v), data in edges_data.items()],
    columns=['source', 'target', 'weight']
)

print(edge_list)
