
import networkx as nx

def create_graph_from_description(graph_description):
    G = nx.Graph()
    
    for edge in graph_description:
        G.add_edge(edge[0], edge[1])
    
    return G

graph_description = [(1, 2), (2, 3), (3, 1)]
small_graph = create_graph_from_description(graph_description)

print(nx.info(small_graph))
