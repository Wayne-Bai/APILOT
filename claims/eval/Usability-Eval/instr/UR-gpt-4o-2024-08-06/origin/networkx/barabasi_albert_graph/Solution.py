import networkx as nx
import matplotlib.pyplot as plt

def generate_barabasi_albert_graph(n, m):
    """
    Generates a Barabási–Albert (BA) random graph.
    
    Parameters:
    n (int): Number of nodes in the graph.
    m (int): Number of edges to attach from a new node to existing nodes.

    Returns:
    G: Generated BA graph.
    """
    # Generate the BA graph with n nodes and m edges
    G = nx.barabasi_albert_graph(n, m)
    
    return G

# Parameters for the BA model
num_nodes = 20  # Total number of nodes
num_edges = 2   # Number of edges to attach from a new node to existing nodes

# Generate graph
ba_graph = generate_barabasi_albert_graph(num_nodes, num_edges)

# Draw the graph
nx.draw(ba_graph, with_labels=True, node_color='skyblue', edge_color='gray', node_size=500)
plt.title("Barabási–Albert Graph")
plt.show()
