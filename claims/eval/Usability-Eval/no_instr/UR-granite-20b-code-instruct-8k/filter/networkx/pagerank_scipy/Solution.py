import networkx as nx

# Define your graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(['A', 'B', 'C', 'D'])
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D')])

# Compute PageRank
page_rank = nx.pagerank(G)

# Print the PageRank of each node
for node, rank in page_rank.items():
    print(f"The PageRank of node {node} is {rank}")
