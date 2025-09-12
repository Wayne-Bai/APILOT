import networkx as nx

def calculate_pagerank(graph):
    # Calculate PageRank of the nodes in the given graph
    pagerank_dict = nx.pagerank(graph)
    return pagerank_dict

# Example usage:
G = nx.DiGraph()  # Create a directed graph
G.add_edges_from([(1, 2), (2, 3), (3, 1), (4, 3)])  # Add edges to the graph

pagerank = calculate_pagerank(G)
print("PageRank of nodes:", pagerank)
