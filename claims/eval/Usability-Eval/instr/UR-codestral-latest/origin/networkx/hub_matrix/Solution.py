import networkx as nx

# Assuming that 'G' is your existing graph
hubs, authorities = nx.hits(G)

print("Hub Matrix:")
for node, hub_score in hubs.items():
    print(f"Node {node}: {hub_score}")
