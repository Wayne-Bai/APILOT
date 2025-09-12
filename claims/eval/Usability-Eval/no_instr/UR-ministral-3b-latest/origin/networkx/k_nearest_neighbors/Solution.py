import networkx as nx

def average_degree_connectivity(G):
    degree_sequence = {k: v for k, v in G.degree().items()}
    average_degree = sum(degree_sequence.values()) / len(degree_sequence)
    return average_degree

# Example usage:
G = nx.erdos_renyi_graph(n=10, p=0.5)
average_degree = average_degree_connectivity(G)
print("Average Degree Connectivity:", average_degree)
