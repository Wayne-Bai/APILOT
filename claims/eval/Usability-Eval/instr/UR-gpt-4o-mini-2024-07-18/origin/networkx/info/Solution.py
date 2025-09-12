import networkx as nx

def print_graph_summary(G, node=None):
    if node is not None:
        if node in G:
            print(f"Summary for node {node}:")
            print(f"Degree: {G.degree(node)}")
            print(f"Neighbors: {list(G.neighbors(node))}")
            print(f"Number of neighbors: {len(list(G.neighbors(node)))})")
        else:
            print(f"Node {node} not found in the graph.")
    else:
        print("Summary for the entire graph:")
        print(f"Number of nodes: {G.number_of_nodes()}")
        print(f"Number of edges: {G.number_of_edges()}")
        print(f"Nodes: {list(G.nodes())}")
        print(f"Edges: {list(G.edges())}")

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])
# print_graph_summary(G)
# print_graph_summary(G, node=1)
