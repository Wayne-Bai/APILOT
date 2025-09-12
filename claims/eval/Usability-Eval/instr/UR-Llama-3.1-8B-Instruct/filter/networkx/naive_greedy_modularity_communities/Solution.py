# Import necessary libraries
import networkx as nx
import community

# Create an empty graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (2, 5), (5, 6), (6, 2), (5, 7), (7, 8), (8, 5)])

# Move nodes with highest modularity scores to the next level down
partition = community.best_partition(G)

# Create a dictionary to store the community assignments
community_assignments = {}

# Iterate over each node and get its community assignment
for node in G.nodes():
    community_assignments[node] = partition[node]

# Create a new graph with communities as nodes
community_graph = nx.Graph()

# Iterate over each community and add nodes to the community graph
for community in set(community_assignments.values()):
    community_graph.add_node(community)

# Iterate over each edge in the original graph
for edge in G.edges():
    # Get the community assignments of the nodes in the edge
    community1 = community_assignments[edge[0]]
    community2 = community_assignments[edge[1]]
    
    # Add an edge to the community graph between the two communities
    community_graph.add_edge(community1, community2)

# Print the community graph
print(community_graph.edges())

# Calculate the modularity of the community graph
modularity = nx.modularity(community_graph)

# Print the modularity of the community graph
print("Modularity:", modularity)
