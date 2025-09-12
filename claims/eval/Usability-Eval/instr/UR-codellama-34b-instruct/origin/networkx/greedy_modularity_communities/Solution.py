
import networkx as nx

# Define the graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(['A', 'B', 'C'])
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('A', 'C')

# Find communities in the graph using greedy modularity maximization
communities = nx.greedy_modularity_communities(G)

# Print the communities found
print("Communities:", communities)
