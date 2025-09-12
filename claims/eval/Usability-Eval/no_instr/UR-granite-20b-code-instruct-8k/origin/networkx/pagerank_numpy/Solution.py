import networkx as nx
# create an instance of graph
G = nx.Graph()
# add edges to the graph
G.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10)])
# calculate PageRank
nx.pagerank(G)
