import networkx as nx

# A list of paths to create a directed prefix tree from
paths = [['A', 'B'], ['A', 'B', 'C'], ['D', 'E', 'F'], ['D', 'G']]

# Create a new directed graph using NetworkX
G = nx.DiGraph()

# Add nodes and edges by iterating through the paths list
for path in paths:
    for i in range(len(path) - 1):
        G.add_edge(path[i], path[i+1])

# Display the directed prefix tree
print(nxagraph(G))
