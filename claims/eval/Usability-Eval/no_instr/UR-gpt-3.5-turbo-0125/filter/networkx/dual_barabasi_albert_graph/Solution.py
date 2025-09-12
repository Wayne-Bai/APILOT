
# Importing the networkx library
import networkx as nx

# Function to generate a random graph using dual Barabási–Albert preferential attachment
def dual_barabasi_albert_graph(n, m1, m2, seed=None):
    G = nx.empty_graph(m1)
    G.add_edges_from(nx.barabasi_albert_graph(n-m1, m1, seed=seed).edges())
    G.add_edges_from(nx.barabasi_albert_graph(n-m1, m2, seed=seed).edges())
    return G

# Generate a random graph using dual Barabási–Albert preferential attachment with 100 nodes, m1=3, m2=2
random_graph = dual_barabasi_albert_graph(100, 3, 2)

print(random_graph.nodes())
print(random_graph.edges())
