import networkx as nx

def has_eulerian_path(G, source=None):
    if not G.is_directed():
        # For undirected graphs
        odd_degree_nodes = [node for node, degree in G.degree() if degree % 2 != 0]
        if len(odd_degree_nodes) == 0:
            return True
        elif len(odd_degree_nodes) == 2:
            if source is None:
                return True
            else:
                return source in odd_degree_nodes
        else:
            return False
    else:
        # For directed graphs
        in_degrees = dict(G.in_degree())
        out_degrees = dict(G.out_degree())
        
        start_nodes = [node for node in G.nodes() if out_degrees[node] - in_degrees[node] == 1]
        end_nodes = [node for node in G.nodes() if in_degrees[node] - out_degrees[node] == 1]
        other_nodes = [node for node in G.nodes() if in_degrees[node] == out_degrees[node]]
        
        if len(start_nodes) == 1 and len(end_nodes) == 1 and len(other_nodes) == len(G) - 2:
            if source is None:
                return True
            else:
                return source == start_nodes[0]
        else:
            return False

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 1)])
# print(has_eulerian_path(G))  # Output: True
