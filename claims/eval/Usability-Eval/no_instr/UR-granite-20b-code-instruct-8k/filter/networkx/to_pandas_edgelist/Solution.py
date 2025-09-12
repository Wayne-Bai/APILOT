import pandas as pd
import networkx as nx

# generate graph edge list as a Pandas DataFrame
edge_list_df = pd.DataFrame(nx.convert.to_pandas_edgelist(G))
