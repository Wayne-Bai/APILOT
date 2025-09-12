import networkx as nx

def create_small_graph(graph_description):
    G = nx.Graph()

    # Add nodes
    G.add_node("A")
    G.add_node("B")
    G.add_node("C")
    G.add_node("D")

    # Add edges
    G.add_edge("A", "B")
    G.add_edge("A", "C")
    G.add_edge("B", "D")

    return G

# Example usage:
graph_description = "A graph with 4 nodes and 3 edges"
G = create_small_graph(graph_description)

# Print the graph
print(G.edges())
