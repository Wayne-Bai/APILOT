import networkx as nx

# Returns a random graph using Barabasi-Albert preferential attachment
def generate_random_graph(n, m):
    G = nx.barabasi_albert_graph(n, m)
    return G
