# Import the necessary libraries
import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')

# Add edges to the graph with their respective weights
G.add_edge('A', 'B', weight=2)
G.add_edge('A', 'C', weight=4)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=7)
G.add_edge('C', 'D', weight=3)
G.add_edge('C', 'E', weight=5)
G.add_edge('D', 'E', weight=6)

# Compute the shortest paths between nodes
shortest_paths = nx.floyd_warshall(G)

# Print the shortest paths
print('Shortest paths:')
for node in shortest_paths:
    for other_node in shortest_paths[node]:
        if node!= other_node:
            print(f'Shortest path from {node} to {other_node}: {shortest_paths[node][other_node]}')

# Alternatively, you can also use dijkstra's shortest path algorithm
# Compute the shortest paths from a specific node
start_node = 'A'
shortest_paths = nx.single_source_dijkstra_path_length(G, start_node)

# Print the shortest paths
print('\nShortest paths from node A:')
for node in shortest_paths:
    print(f'Shortest path from {start_node} to {node}: {shortest_paths[node]}')

# Draw the graph to visualize the shortest paths
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
