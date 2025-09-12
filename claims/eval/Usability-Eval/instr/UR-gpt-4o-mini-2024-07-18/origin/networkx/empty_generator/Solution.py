
import networkx as nx

# Create an empty directed graph
G = nx.DiGraph()

# Alternatively, for an undirected graph, use:
# G = nx.Graph()

# This creates an empty generator object for the created graph.
generator = nx.generators.random_graphs.empty_graph()

# Note that the generator is an empty graph, and can be used to generate additional graphs if needed.
