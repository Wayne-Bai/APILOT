import networkx as nx
# create a graph
G = nx.Graph()
# add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])
# compute shortest path lengths to target node 4 from all reachable nodes
shortest_path_lengths = nx.single_source_shortest_path_length(G, source=4)
# print the shortest path lengths
for node, length in shortest_path_lengths.items():
 print(f"Shortest path length to node {node}: {length}")
