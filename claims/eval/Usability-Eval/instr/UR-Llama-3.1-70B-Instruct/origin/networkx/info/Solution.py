import networkx as nx

def print_graph_summary(G=None, n=None):
    if G is None:
        raise ValueError("Graph is required to print summary")

    if n is not None:
        # Node summary
        neighbors = list(G.neighbors(n))
        degree = G.degree(n)
        print(f"Node: {n}")
        print(f"Neighbors: {neighbors}")
        print(f"Degree: {degree}")
    else:
        # Graph summary
        nodes = G.number_of_nodes()
        edges = G.number_of_edges()
        density = nx.density(G)
        is_directed = nx.is_directed(G)
        is_weighted = any('weight' in G.get_edge_data(edge[0], edge[1]) for edge in G.edges())
        
        print("Graph Summary:")
        print(f"Number of Nodes: {nodes}")
        print(f"Number of Edges: {edges}")
        print(f"Density: {density:.2f}")
        print(f"Is Directed: {is_directed}")
        print(f"Is Weighted: {is_weighted}")

# Example usage:
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])

print_graph_summary(G)
print_graph_summary(G, 1)
