
import networkx as nx

# Create a seed node for the graph
seed_node = nx.utils.powerlaw_sequence(1, 2)

# Define the Barabasi-Albert preferential attachment model
model = nx.generators.barabasi_albert_graph(seed_node, m=3)

# Generate a random graph using the model
G = nx.gnp_random_graph(50, 0.4)
