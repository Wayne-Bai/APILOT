import networkx as nx

def has_eulerian_path(G, source=None):
    odd_degree_nodes = [n for n, d in G.degree() if d % 2 != 0]

    if not odd_degree_nodes:  # If there are no nodes with odd degree
        if source is None:
            return True
        else:
            # Check if the source degree is even
            return G.has_eulerian_path(source)
    elif len(odd_degree_nodes) == 2:  # If there is exactly one node start and one node end
        return nx.has_eulerian_path(G, start=odd_degree_nodes[0], end=odd_degree_nodes[1])
    else:  # If there are more than 2 nodes with odd degree
        return False

# Example usage:
if __name__ == "__main__":
    G = nx.Graph()
    edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4), (4, 5), (5, 3)]
    G.add_edges_from(edges)
    print(has_eulerian_path(G))
    # If you need to check starting from a specific node, uncomment the following line
    # print(has_eulerian_path(G, source=0))
