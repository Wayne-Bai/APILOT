import networkx as nx

def print_graph_summary(G, node=None):
    graph_summary = "Graph Summary:" if node is None else f"Node Summary for {node}:"

    print(f"{graph_summary}")
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")

    if node:
        print(f"Degree of {node}: {G.degree(node)}")
        print(f"Neighbors of {node}: {list(G.neighbors(node))}")

# Example usage:
# G = nx.erdos_renyi_graph(5, 0.5)  # Example graph
# print_graph_summary(G)
