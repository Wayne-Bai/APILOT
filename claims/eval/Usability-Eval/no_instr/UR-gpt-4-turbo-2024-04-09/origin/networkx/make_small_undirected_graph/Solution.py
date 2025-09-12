import networkx as nx

def create_graph():
    # Create an empty undirected graph
    G = nx.Graph()

    # Add nodes and edges based on a hypothetical description
    nodes = ['A', 'B', 'C', 'D']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C')]

    # Add nodes and edges to the graph
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    
    return G

# Create the graph
graph = create_graph()

# Print the nodes and edges of the graph
print("Nodes:", graph.nodes())
print("Edges:", graph.edges())
