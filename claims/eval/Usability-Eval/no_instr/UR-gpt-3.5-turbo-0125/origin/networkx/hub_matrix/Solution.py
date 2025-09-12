
import networkx as nx

G = nx.DiGraph()
# Add nodes and edges to the graph G

hubs, _ = nx.hits(G)
hub_matrix = [hubs[node] for node in G.nodes()]

print(hub_matrix)
