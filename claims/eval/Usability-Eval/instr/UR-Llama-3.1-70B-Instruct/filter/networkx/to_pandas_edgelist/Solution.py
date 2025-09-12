import networkx as nx
import pandas as pd

def get_edge_list(G):
    edge_list = []
    for edge in G.edges():
        source_node = edge[0]
        target_node = edge[1]
        if G.is_directed():
            edge_list.append({'source': source_node, 'target': target_node})
        else:
            if source_node < target_node:
                edge_list.append({'source': source_node, 'target': target_node})
            else:
                edge_list.append({'source': target_node, 'target': source_node})
    
    return pd.DataFrame(edge_list)

# Create an empty directed graph
G = nx.DiGraph()

# Add edges
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')

# Print the edge list
print(get_edge_list(G))

# Create an empty undirected graph
G = nx.Graph()

# Add edges
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')

# Print the edge list
print(get_edge_list(G))
