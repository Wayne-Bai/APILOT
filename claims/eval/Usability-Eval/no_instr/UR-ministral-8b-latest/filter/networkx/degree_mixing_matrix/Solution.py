import networkx as nx

def fugate_matrix(Graph):
    R = {}
    for node in Graph.nodes:
        R[node] = (nx.field_node_attribute(Graph, node),)
    return R

# Create a sample graph with networkx
G = nx.Graph()
G.add_node(1, value='A')
G.add_node(2, value='B')
G.add_node(3, value='C')

# Call the function to get the mixing matrix
mixing_matrix = fugate_matrix(G)
print(mixing_matrix)
