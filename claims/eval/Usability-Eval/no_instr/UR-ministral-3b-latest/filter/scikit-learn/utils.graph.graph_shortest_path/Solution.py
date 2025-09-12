from sklearn.datasets import make_graph

# Generating a random graph
data, adjacency_matrix = make_graph()

# Performing the shortest-path graph search
# Note: Scikit-learn does not have a 'graph shortest path search' method, so this will be a general approach

import networkx as nx

G = nx.Graph()
for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix)):
        if adjacency_matrix[i][j] > 0:
            G.add_edge(i, j, weight=adjacency_matrix[i][j])

# Now, you can use networkx to find the shortest path
start_node = 0
end_node = len(adjacency_matrix) - 1

shortest_path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')

print(f"Shortest path from node {start_node} to node {end_node}: {shortest_path}")
