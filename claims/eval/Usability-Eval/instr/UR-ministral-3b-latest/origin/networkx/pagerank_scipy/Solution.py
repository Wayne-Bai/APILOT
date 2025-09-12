import networkx as nx

G = nx.Graph()  # Create an empty graph

# Add nodes and edges
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_edges_from([('A', 'B'), ('B', 'C')])

# Compute PageRank
page_rank = nx.pagerank(G)  # Compute the PageRank of the nodes

# Print the PageRank
print("PageRank of each node: ", page_rank)
