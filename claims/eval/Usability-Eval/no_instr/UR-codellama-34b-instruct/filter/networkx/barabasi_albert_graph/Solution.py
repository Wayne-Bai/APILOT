import networkx as nx

# Define the number of nodes and edges in the graph
n = 100
m = 25

# Create a directed or undirected graph with the specified number of nodes and edges
G = nx.gnp_random_graph(n, m)

# Set the preferential attachment parameter for the Barabási-Albert model
pa = 10

# Generate the random graph using the Barabási-Albert preferential attachment model
nx.barabasi_albert_model(G, pa)
