import networkx as nx
graph = nx.karate_club_graph()  # Example graph
google_matrix = nx.to_numpy_matrix(graph, nodelist=graph.nodes())  # Converts the graph to a numpy matrix
print(google_matrix)
