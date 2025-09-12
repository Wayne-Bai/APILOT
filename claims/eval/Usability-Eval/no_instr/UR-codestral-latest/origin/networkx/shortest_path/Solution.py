import networkx as nx

# Assuming G is your graph and source, target are your nodes
# If you don't have a graph, you can create one like so:
# G = nx.Graph()
# G.add_edge('source', 'target', weight=1)  # replace 1 with your weight

# Calculate the shortest path
shortest_path = nx.shortest_path(G, source=source, target=target)

print(f"The shortest path from {source} to {target} is: {shortest_path}")
