
import networkx as nx

def barabasi_albert_graph(n, m):
    # Create an empty graph
    G = nx.Graph()
    
    # Add the first node
    G.add_node(0)
    
    for i in range(1, n):
        # Select a random neighbor of the previous node with probability m/i
        if np.random.rand() < m/i:
            # If the random number is less than m/i, add a new node and make it a neighbor of the previous node
            G.add_node(i)
            G.add_edge(i-1, i)
            
    return G
