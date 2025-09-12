import networkx as nx

def print_graph_summary(G):
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Is directed: {'Yes' if G.is_directed() else 'No'}")
    print(f"Is weighted: {'Yes' if any(data.get('weight') for _, _, data in G.edges(data=True)) else 'No'}")
    print(f"Density: {nx.density(G)}")

def print_node_summary(G, n):
    if n in G:
        print(f"Node {n} is in the graph.")
        print(f"Degree of node {n}: {G.degree(n)}")
        print(f"Neighbors of node {n}: {list(G.neighbors(n))}")
    else:
        print(f"Node {n} is not in the graph.")

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 4)])
# print_graph_summary(G)
# print_node_summary(G, 2)
