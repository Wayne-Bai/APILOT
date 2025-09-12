
from networkx import Graph

def has_eulerian_path(G):
    # check if G is a directed graph
    if not G.is_directed():
        raise ValueError("Graph must be directed")

    # count the number of edges and nodes in the graph
    num_edges = G.number_of_edges()
    num_nodes = G.number_of_nodes()

    # check if the graph is connected
    if not nx.is_connected(G):
        return False

    # check if the graph has an even number of edges and nodes
    if num_edges % 2 != 0 or num_nodes % 2 != 0:
        return False

    # check if the graph has a source node
    source = nx.source(G)
    if source is None:
        return False

    # create a new graph with all edges reversed
    G_reversed = G.reverse()

    # find the shortest path between the source and all other nodes in the graph
    shortest_paths = nx.shortest_paths(G_reversed, source)

    # check if there is a shortest path to every other node in the graph
    for target in G:
        if not shortest_paths[target]:
            return False

    # if we get this far, then the graph has an Eulerian path
    return True
