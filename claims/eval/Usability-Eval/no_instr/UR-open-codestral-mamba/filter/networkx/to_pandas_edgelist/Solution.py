import networkx as nx
import pandas as pd

# Create a graph
G = nx.Graph()

# Add edges to the graph
G.add_edge('Node1', 'Node2')
G.add_edge('Node2', 'Node3')
G.add_edge('Node3', 'Node4')

# Convert the edge list to a DataFrame
edge_list = list(G.edges())
df = pd.DataFrame(edge_list, columns=['Source', 'Target'])

print(df)
