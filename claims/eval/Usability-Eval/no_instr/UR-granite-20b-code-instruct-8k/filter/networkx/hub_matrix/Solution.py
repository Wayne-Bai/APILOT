import networkx as nx

# Define the graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(2, 5)
G.add_edge(3, 4)
G.add_edge(3, 6)
G.add_edge(4, 7)
G.add_edge(5, 7)
G.add_edge(6, 7)

# Compute the HITS hub and authority scores
hub_scores, authority_scores = nx.hits(G)

# Print the results
print("Hub scores:")
for node, score in hub_scores.items():
    print(f"{node}: {score}")

print("\nAuthority scores:")
for node, score in authority_scores.items():
    print(f"{node}: {score}")
