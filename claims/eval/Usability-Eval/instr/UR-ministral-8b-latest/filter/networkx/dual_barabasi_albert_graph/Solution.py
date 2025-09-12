import networkx as nx
import random

# Set random seed for reproducibility
random.seed(42)

def generate_dual_barabasi_albert_graph(n1, n2, m):
    # Create the first graph with n1 vertices
    G1 = nx.ERG(n1, p=2/m)
    # Create the second graph with n2 vertices
    G2 = nx.ERG(n2, p=2/m)

    # Add connected edges between graphs
    for node in list(G1.nodes()):
        if random.random() < 2/m:
            G2.add_edge(node, random.choice(list(G2.nodes())))

    return nx.union(G1, G2)

# Example usage
n1, n2, m = 10, 15, 0.1
graph = generate_dual_barabasi_albert_graph(n1, n2, m)
print(nx.density(graph))  # Prints the density of the resulting graph
