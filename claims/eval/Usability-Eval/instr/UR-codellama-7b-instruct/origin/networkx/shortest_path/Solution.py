
import networkx as nx

# create a simple directed graph
G = nx.DiGraph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')])

# compute shortest paths between nodes A and B
paths = nx.shortest_paths(G, source='A', target='B')

# print the shortest path
print(paths)
