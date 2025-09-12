import networkx as nx

# your code here
graph = nx.Graph()  # create a graph object
# add nodes and edges to the graph object
# ...

adjacency_matrix = nx.to_numpy_matrix(graph)  # convert the graph adjacency matrix to a NumPy matrix
print(adjacency_matrix)
