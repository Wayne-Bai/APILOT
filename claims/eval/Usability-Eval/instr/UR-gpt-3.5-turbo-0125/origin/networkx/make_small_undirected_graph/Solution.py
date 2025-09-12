
import networkx as nx

def create_graph_from_description(graph_description):
    G = nx.Graph()
    if graph_description == "example":
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
    # Add more graph descriptions as needed

    return G

graph_description = "example"
small_graph = create_graph_from_description(graph_description)
print("Nodes of the graph:", small_graph.nodes())
print("Edges of the graph:", small_graph.edges())
