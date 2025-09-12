
import networkx as nx

# Returns a random graph using Barabási–Albert preferential attachment
def generate_barabasi_albert_graph(nodes, edges_to_attach):
    G = nx.barabasi_albert_graph(nodes, edges_to_attach)
    return G
