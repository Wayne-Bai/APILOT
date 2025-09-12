# Import necessary libraries
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Add edges
G.add_edges_from([(1,2), (1,3), (2,3), (2,4), (3,4), (4,5), 
                  (5,6), (5,7), (6,7), (6,8), (7,8), 
                  (8,9), (8,10), (9,10)])

# Find communities in G using greedy modularity maximization
from networkx.algorithms.community import greedy_modularity_communities
communities = list(greedy_modularity_communities(G))

# Print the communities
community_no = 1
for community in communities:
    print(f"Community {community_no}: {list(community)}")
    community_no += 1

# Draw the graph with communities
colors = ['r', 'g', 'b', 'y','m', 'c', 'k']
colors_idx = 0
pos = nx.spring_layout(G)
for community in communities:
    nx.draw_networkx_nodes(G, pos, nodelist=community, node_color=colors[colors_idx])
    colors_idx = (colors_idx + 1) % len(colors)
nx.draw_networkx_edges(G, pos)
plt.show()
