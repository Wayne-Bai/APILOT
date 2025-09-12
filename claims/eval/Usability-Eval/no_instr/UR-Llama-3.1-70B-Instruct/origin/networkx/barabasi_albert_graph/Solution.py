import networkx as nx
import matplotlib.pyplot as plt

def generate_barabasi_albert_graph(n, m, seed=None):
    """
    Returns a random graph using Barabási–Albert preferential attachment.

    Parameters:
    n (int): Number of nodes.
    m (int): Number of edges to connect each new node to existing nodes.
    seed (int): Seed for random number generation (optional).

    Returns:
    G (nx.Graph): A random graph using Barabási–Albert preferential attachment.
    """
    # Create a new empty graph
    G = nx.Graph()

    # Add m initial nodes
    G.add_nodes_from(range(m))

    # Add edges between initial nodes
    for i in range(m):
        for j in range(i+1, m):
            G.add_edge(i, j)

    # Add remaining nodes
    for i in range(m, n):
        # Choose m nodes to connect to
        # Preferential attachment based on node degree
        new_edges = nx.preferential_attachment(G, m)
        
        # Add new node and edges
        G.add_node(i)
        for j in new_edges:
            G.add_edge(i, j)

    return G

# Example usage
n = 10
m = 2

G = generate_barabasi_albert_graph(n, m)

# Draw the graph
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=12)
plt.show()
