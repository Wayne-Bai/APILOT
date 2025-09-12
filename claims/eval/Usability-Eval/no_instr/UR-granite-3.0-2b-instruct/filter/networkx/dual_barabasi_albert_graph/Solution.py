import networkx as nx
import random

def generate_random_graph(num_nodes, num_edges):
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))

    # Initialize node degrees
    degrees = [random.randint(1, 5) for _ in range(num_nodes)]

    # Generate edges based on Barabási–Albert preferential attachment
    for _ in range(num_edges):
        # Find the next node to connect to
        next_node = random.choice(list(G.nodes()))

        # Update the degree of the next node
        degrees[next_node] += 1

        # Connect the current node to the next node
        G.add_edge(random.choice(list(G.nodes())), next_node)

    # Update node degrees based on the new connections
    for node, degree in zip(G.nodes(), degrees):
        G.nodes[node]['degree'] = degree

    return G

# Example usage:
G = generate_random_graph(100, 50)
