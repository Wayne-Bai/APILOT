import networkx as nx
import numpy as np

# Create a new directed graph
G = nx.DiGraph()

# Add nodes to the graph
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")

# Add edges to the graph
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "A")
G.add_edge("C", "D")
G.add_edge("D", "A")
G.add_edge("D", "B")

# Compute the PageRank of the nodes in the graph
pr = nx.pagerank(G)

# Print the PageRank of each node
print("PageRank of the nodes:")
for node, rank in pr.items():
    print(f"{node}: {rank:.4f}")

# Alternatively, you can also use the pagerank function with a personalization vector
personalization = {"A": 1.0, "B": 0.5, "C": 0.5, "D": 0.0}
pr_personalized = nx.pagerank(G, personalization=personalization)
print("\nPageRank of the nodes with personalization:")
for node, rank in pr_personalized.items():
    print(f"{node}: {rank:.4f}")
