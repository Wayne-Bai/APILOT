import networkx as nx
import community

# Create a sample networkx graph
G = nx.karate_club_graph()

# Use the community library to find the communities
partition = community.best_partition(G)

# Print the community IDs of each node
print(partition)

# Alternatively, you can use the community generation method
# partition = community.generate.correct_partitions(G, [1])
# Alternatively, you can use the greedy method
# partition = community.best_partition(G) 

# To get a dictionary where the keys are the node IDs and the values are lists of their community IDs
community_dict = {}
for node in G.nodes():
    community_dict[node] = [partition[node]]

# To get a dictionary where the keys are the community IDs and the values are lists of their member node IDs
community_dict = {}
for node in G.nodes():
    if not community_dict.get(partition[node]):
        community_dict[partition[node]] = [node]
    else:
        community_dict[partition[node]].append(node)

print(community_dict)
