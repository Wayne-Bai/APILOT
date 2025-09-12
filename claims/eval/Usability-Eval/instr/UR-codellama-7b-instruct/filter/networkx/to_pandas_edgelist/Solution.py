
import pandas as pd
import networkx as nx

# create a simple graph
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C'])
G.add_edges_from([('A', 'B'), ('B', 'C')])

# convert the graph to a Pandas DataFrame
df = pd.DataFrame(nx.to_pandas_edgelist(G))
