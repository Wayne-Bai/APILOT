import networkx as nx

def print_graph_info(G):
    """
    Function to print summary of information for the graph G.
    Parameters:
    ----------
    G: networkx graph
    """
    print(f'Number of nodes: {G.number_of_nodes()}')
    print(f'Number of edges: {G.number_of_edges()}')
    print(f'Graph is directed: {G.is_directed()}')
    print(f'Density of the graph: {nx.density(G)}')

def print_node_info(G, n):
    """
    Function to print summary of information for the node n.
    Parameters:
    ----------
    G: networkx graph
    n: node in the graph
    """
    if n not in G.nodes():
        print(f'Node {n} does not exist in the graph')
        return
    neighbors = list(G.neighbors(n))
    print(f'Neighbors of node {n}: {neighbors}')
    print(f"Degree of node {n}: {G.degree(n)}")

# Test the functions
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

print_graph_info(G)
print_node_info(G, 2)
