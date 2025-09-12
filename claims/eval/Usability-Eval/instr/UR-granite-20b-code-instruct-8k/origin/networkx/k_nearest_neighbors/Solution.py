import networkx as nx
# create a graph
G = nx.Graph()
# add edges to the graph (optional)
#G.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10)])
# compute the average degree connectivity
avg_degree_connectivity = nx.average_degree_connectivity(G)
print("Average degree connectivity:", avg_degree_connectivity)
