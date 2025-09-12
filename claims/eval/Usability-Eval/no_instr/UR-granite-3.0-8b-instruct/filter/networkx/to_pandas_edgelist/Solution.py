import networkx as nx
import pandas as pd

# Assuming G is your graph
edge_list = list(G.edges())

# Create a DataFrame from the edge list
df = pd.DataFrame(edge_list, columns=['Node1', 'Node2'])
