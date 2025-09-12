import networkx as nx

def print_graph_summary(G):
    print("Graph Summary:")
    print("Number of nodes:", G.number_of_nodes())
    print("Number of edges:", G.number_of_edges())
    print("Nodes:", G.nodes())
    print("Edges:", G.edges())
    
def print_node_summary(G, n):
    if n in G:
        print(f"Node Summary for {n}:")
        print("Neighbors:", list(G.neighbors(n)))
        print("Degree:", G.degree(n))
    else:
        print(f"Node {n} is not in the graph.")

# Example usage:
# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4)])

# Print summary for the entire graph
print_graph_summary(G)

# Print summary for a specific node
print_node_summary(G, 2)
