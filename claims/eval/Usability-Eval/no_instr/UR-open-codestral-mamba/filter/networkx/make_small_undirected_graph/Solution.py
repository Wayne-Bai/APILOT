import networkx as nx

# Define the graph description
graph_description = [(1, 2, 'edge1'), (2, 3, 'edge2'), (3, 1, 'edge3'), (4, 2, 'edge4'), (4, 3, 'edge5')]

# Create an empty graph
G = nx.Graph()

# Add edges to the graph based on the description
for edge in graph_description:
    G.add_edge(edge[0], edge[1], label=edge[2])

# Print the adjacency list of the graph
print(dict(nx.adjacency_list(G)))
