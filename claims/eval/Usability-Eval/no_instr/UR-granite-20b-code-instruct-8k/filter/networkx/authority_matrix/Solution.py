
import networkx as nx
# create an instance of the graph
G = nx.Graph()
# define the edges and their weights
G.add_edge("A", "B", weight=0.5)
G.add_edge("B", "C", weight=0.3)
G.add_edge("C", "D", weight=0.9)
G.add_edge("D", "A", weight=0.7)
# compute the HITS authority matrix
hits = nx.hits(G)
# print the authority matrix
print(hits. authority_matrix())
