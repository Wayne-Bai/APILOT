import networkx as nx
import numpy as np

# Create a new directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'A')
G.add_edge('B', 'D')
G.add_edge('C', 'A')
G.add_edge('C', 'F')
G.add_edge('D', 'B')
G.add_edge('E', 'B')
G.add_edge('F', 'C')

# Compute PageRank
pr = nx.page_rank(G, alpha=0.85)

# Print the PageRank
print("PageRank:")
for node, rank in pr.items():
    print(f"{node}: {rank}")

# Normalize PageRank
sum_pr = sum(pr.values())
normalized_pr = {node: rank / sum_pr for node, rank in pr.items()}

# Print the normalized PageRank
print("\nNormalized PageRank:")
for node, rank in normalized_pr.items():
    print(f"{node}: {rank}")
