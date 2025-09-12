import networkx as nx
import pandas as pd

# Assume G is the graph
# Creating a graph
G = nx.Graph()
# Adding some edges to the graph
G.add_edges_from([('A', 'B'), ('B', 'C'), ('A', 'C'), ('D', 'A'), ('D', 'C')])

# Extracting the edge list as a DataFrame
edge_list = pd.DataFrame(list(G.edges), columns=['Source', 'Target'])
edge_list
