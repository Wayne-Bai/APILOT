import networkx as nx
import random

# Generate a random graph using Barabási-Albert preferential attachment
def generate_random_graph(n):
    G = nx.gnp_random_graph(n, 0.1)  # create an empty graph with n nodes
    for iteration in range(n):
        new_node = [node for node in G.nodes()]
        new_edge_probabilities = [G.degree() for node in new_node]
        new_edge_probabilities = [p/sum(new_edge_probabilities) for p in new_edge_probabilities]
        parent_node = random.choices(new_node, weights=new_edge_probabilities)[0]
        G.add_node(iteration + 1)
        G.add_edge(iteration + 1, parent_node)
    return G

# Example usage
n = 100
random_graph = generate_random_graph(n)
print(f"Generated graph with {random_graph.nodes()} nodes.")
