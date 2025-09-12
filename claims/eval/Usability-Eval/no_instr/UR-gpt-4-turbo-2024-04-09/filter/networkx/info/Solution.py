import networkx as nx

def print_graph_summary(G, n=None):
    if n is None:
        # Print information about the whole graph
        print(nx.info(G))
    else:
        # Ensure the node exists in the graph
        if n in G:
            # Print information specific to the node
            print(f"Node {n} has degree {G.degree[n]} with neighbors {list(G.neighbors(n))}")
        else:
            print(f"Node {n} does not exist in the graph.")

# Example Usage
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (1, 3)])

print_graph_summary(G)          # Prints summary of the whole graph
print_graph_summary(G, n=1)     # Prints information about node 1
