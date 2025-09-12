import networkx as nx
import random

def generate_random_graph(n, m):
    G = nx.Graph()
    G.add_nodes_from(range(n))

    # Initialize node degrees
    degrees = [random.randint(m, 2*m) for _ in range(n)]

    # Add nodes one by one
    for i in range(n):
        # Find the nearest neighbor
        nearest_neighbor = random.choice([j for j in G.nodes() if j != i])

        # Add a new node with degree one
        G.add_node(n+i)

        # Update the degree of the nearest neighbor
        degrees[nearest_neighbor] += 1

        # Update the degree of the new node
        degrees[i] -= 1

    # Add the new edges
    for i in range(n):
        for _ in range(degrees[i]):
            j = random.choice([k for k in G.nodes() if k != i])
            G.add_edge(i, j)

    return G
