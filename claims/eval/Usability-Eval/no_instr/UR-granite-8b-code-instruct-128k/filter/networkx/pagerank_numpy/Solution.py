import networkx as nx

def get_pagerank(graph):
    """
    Return the PageRank of the nodes in the graph G.

    Parameters
    ----------
    graph : networkx.Graph
        The graph to calculate the PageRank for.

    Returns
    -------
    dict
        A dictionary containing the PageRank for each node in the graph.

    """
    return nx.pagerank(graph)
