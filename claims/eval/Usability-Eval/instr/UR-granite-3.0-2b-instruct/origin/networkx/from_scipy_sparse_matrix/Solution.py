import networkx as nx

# Assuming 'adj_list' is your scipy sparse matrix adjacency list
# Convert the adjacency list to a dictionary
adj_dict = {i: [] for i in range(len(adj_list))}
for i, row in enumerate(adj_list):
    for j, val in enumerate(row):
        if val != 0:
            adj_dict[i].append(j)

# Create a graph from the dictionary
G = nx.Graph()
for node, neighbors in adj_dict.items():
    G.add_node(node)
    for neighbor in neighbors:
        G.add_edge(node, neighbor)
