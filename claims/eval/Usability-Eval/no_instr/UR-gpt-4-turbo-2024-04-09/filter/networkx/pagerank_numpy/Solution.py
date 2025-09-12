import networkx as nx

def calculate_pagerank(G):
    pagerank_dict = nx.pagerank(G)
    return pagerank_dict

# Example usage
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 1), (3, 2)])

pagerank = calculate_pagerank(G)
print(pagerank)
