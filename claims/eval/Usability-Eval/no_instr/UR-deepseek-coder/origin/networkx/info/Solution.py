import networkx as nx

def print_summary(G, node=None):
    if node is None:
        # Summary for the entire graph
        print(f"Graph Summary:")
        print(f"Number of nodes: {G.number_of_nodes()}")
        print(f"Number of edges: {G.number_of_edges()}")
        print(f"Is directed: {'Yes' if G.is_directed() else 'No'}")
        print(f"Is weighted: {'Yes' if nx.is_weighted(G) else 'No'}")
        print(f"Density: {nx.density(G)}")
    else:
        # Summary for a specific node
        if node in G:
            print(f"Node Summary for {node}:")
            print(f"Degree: {G.degree(node)}")
            print(f"Neighbors: {list(G.neighbors(node))}")
            print(f"Clustering Coefficient: {nx.clustering(G, node)}")
        else:
            print(f"Node {node} not found in the graph.")

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 4)])
# print_summary(G)  # Summary for the entire graph
# print_summary(G, 2)  # Summary for node 2
