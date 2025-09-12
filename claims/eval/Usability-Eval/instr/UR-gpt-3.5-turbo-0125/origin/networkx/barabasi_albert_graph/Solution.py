
import networkx as nx

# Generate a random graph using Barabási–Albert preferential attachment
random_graph = nx.barabasi_albert_graph(n=100, m=2, seed=None)

print(random_graph.nodes)
print(random_graph.edges)
