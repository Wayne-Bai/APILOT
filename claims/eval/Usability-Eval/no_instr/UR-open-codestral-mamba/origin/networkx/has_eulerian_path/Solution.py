import networkx as nx

def has_eulerian_path(G, source=None):
    circuits = nx.simple_cycles(G)
    if source is not None:
        circuits = (circuit for circuit in circuits if circuit[0] == source)
    try:
        next(circuits)
    except StopIteration:
        return False
    else:
        return True
