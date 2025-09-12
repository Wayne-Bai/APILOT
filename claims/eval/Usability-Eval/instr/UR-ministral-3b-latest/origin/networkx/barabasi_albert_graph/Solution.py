import networkx as nx

# Create a random graph using Barabási–Albert preferential attachment
G = nx.barabasi_albert_graph(10, 2)

# Print the graph
print(G.nodes(), G.edges())
