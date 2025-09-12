import networkx as nx

def create_small_graph(graph_description):
    G = nx.Graph()
    
    # Example graph description: "A-B, B-C, C-D"
    edges = graph_description.split(", ")
    
    for edge in edges:
        node1, node2 = edge.split("-")
        G.add_edge(node1, node2)
    
    return G

# Example usage:
graph_description = "A-B, B-C, C-D"
small_graph = create_small_graph(graph_description)
print(small_graph.edges())
