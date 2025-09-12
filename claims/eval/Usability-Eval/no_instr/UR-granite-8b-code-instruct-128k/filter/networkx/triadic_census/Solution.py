import networkx as nx

def triadic_census(graph, nodes=None):
    if nodes is None:
        nodes = graph.nodes()
    triangles = 0
    for u in nodes:
        for v in graph.neighbors(u):
            if v in graph.neighbors(v):
                triangles += 1
    return triangles
