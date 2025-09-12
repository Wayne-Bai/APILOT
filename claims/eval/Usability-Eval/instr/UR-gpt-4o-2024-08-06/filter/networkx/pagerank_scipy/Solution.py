import networkx as nx

def compute_pagerank(graph):
    """
    Computes the PageRank of the nodes in a graph using NetworkX.

    :param graph: A NetworkX graph
    :return: A dictionary with nodes as keys and their PageRank as values
    """
    # Compute the PageRank of each node
    pagerank = nx.pagerank(graph)
    return pagerank

# Example usage:
# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph (Example)
G.add_edges_from([
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'A'),
    ('D', 'C')
])

# Get the PageRank of nodes
pagerank_result = compute_pagerank(G)
print(pagerank_result)
