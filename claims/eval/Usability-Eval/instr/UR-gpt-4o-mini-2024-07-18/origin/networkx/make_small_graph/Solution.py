import networkx as nx

def create_small_graph(graph_description):
    G = nx.Graph()
    
    for edge in graph_description:
        G.add_edge(edge[0], edge[1])
    
    return G

# Example usage
graph_description = [(1, 2), (2, 3), (3, 1)]  # Define the edges of the graph
small_graph = create_small_graph(graph_description)

# To visualize or analyze the graph, you can use networkx functions
print(nx.info(small_graph))
