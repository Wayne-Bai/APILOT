
import networkx as nx

# Define the number of nodes and the expected degree distribution
num_nodes = 100
expected_degree_distribution = [0.5, 0.2, 0.1]

# Generate a random graph using Barabási-Albert preferential attachment
G = nx.barabasi_albert_graph(num_nodes, expected_degree_distribution)
