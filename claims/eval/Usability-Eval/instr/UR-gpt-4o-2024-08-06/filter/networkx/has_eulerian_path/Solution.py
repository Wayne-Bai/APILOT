import networkx as nx

def has_eulerian_path(G, source=None):
    # An undirected graph has an Eulerian path if exactly 0 or 2 vertices have odd degree
    if isinstance(G, nx.DiGraph):
        # For directed graph, we need to check if:
        # 1. The graph is strongly connected if it's a directed graph
        # 2. The number of nodes with in_degree = out_degree is exactly n - 2 and 
        #    1 node with in_degree = out_degree + 1 and 
        #    1 node with out_degree = in_degree + 1

        return (sum(1 for v in G.nodes if G.in_degree(v) == G.out_degree(v)) in [G.number_of_nodes(), G.number_of_nodes() - 2] and
                sum(1 for v in G.nodes if G.out_degree(v) == G.in_degree(v) + 1) == 1 and
                sum(1 for v in G.nodes if G.in_degree(v) == G.out_degree(v) + 1) == 1)
    else:
        # For undirected graph, we need to find how many nodes have odd degree
        odd_degree_nodes = sum(1 for v in G.nodes if G.degree(v) % 2 != 0)
        return odd_degree_nodes in [0, 2]

# Example of use
# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 2)])

# Check if it has an Eulerian path
print(has_eulerian_path(G))
