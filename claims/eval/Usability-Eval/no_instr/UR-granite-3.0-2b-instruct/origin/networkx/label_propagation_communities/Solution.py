import networkx as nx

# Assuming G is your graph and labels is a dictionary where keys are nodes and values are their respective labels
G = nx.Graph()
labels = {'A': '1', 'B': '2', 'C': '1', 'D': '2', 'E': '1'}

# Add nodes and edges to your graph
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')])

# Perform label propagation
communities = nx.label_propagation_communities(G,labels=labels)

# Print the communities
for community in communities:
    print(community)
