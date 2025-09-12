import networkx as nx

# Assume G and partition are already defined

# Calculate coverage
coverage = len(set(G.nodes) & set().union(*partition)) / len(G.nodes)

# Calculate performance
cut_size = nx.cut_size(G, partition[0], partition[1])
volume = sum(len(nodes) for nodes in partition)
performance = cut_size / volume if volume > 0 else 0

print(f"Coverage: {coverage}")
print(f"Performance: {performance}")
