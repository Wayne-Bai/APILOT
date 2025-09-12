
import networkx as nx

def create_small_graph():
    G = nx.Graph()

    # Add graph description as edges
    edges = [
        ('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'),
        ('C', 'E'), ('D', 'E'), ('E', 'F')
    ]
    
    G.add_edges_from(edges)
    return G

# Example usage
G = create_small_graph()

print("Nodes of graph: " + str(G.nodes()))
print("Edges of graph: " + str(G.edges()))
