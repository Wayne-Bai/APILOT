import networkx as nx
import pandas as pd

def graph_to_dataframe(G):
    # Create edge list from the graph
    edge_list = list(G.edges(data=True))
    # Create DataFrame
    df = pd.DataFrame(edge_list, columns=['Source', 'Target', 'Attributes'])
    return df

# Example usage
G = nx.Graph()
G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('C', 'A', weight=3)

df = graph_to_dataframe(G)
print(df)
