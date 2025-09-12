import networkx as nx

# Create a graph
G = nx.DiGraph()

# Add nodes and edges
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'E')])

# Calculate PageRank
pr = nx.pagerank(G)

# Print the PageRank of each node
for node, rank in pr.items():
    print(f'Node {node} has PageRank {rank}')
