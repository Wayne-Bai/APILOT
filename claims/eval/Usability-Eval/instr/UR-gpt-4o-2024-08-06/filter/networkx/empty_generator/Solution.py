import networkx as nx

# Create an empty graph
G = nx.Graph()

# Get a generator from the graph (this will be an empty generator since the graph is empty)
generator = (node for node in G.nodes(data=True))

# To demonstrate the generator's usage, one would typically loop or consume it like below:
for node in generator:
    print(node)
