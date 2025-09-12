import networkx as nx

def calculate_pagerank(graph):
    # Calculate PageRank
    pagerank = nx.pagerank(graph)
    return pagerank

# Example of creating a graph and computing its PageRank
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4), (4, 1)])

# Call the calculate_pagerank function
result = calculate_pagerank(G)
print(result)
