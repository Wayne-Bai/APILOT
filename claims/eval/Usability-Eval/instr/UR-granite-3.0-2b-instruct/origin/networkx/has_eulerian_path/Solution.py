import networkx as nx

def has_eulerian_path(G, start=None):
    if not nx.is_connected(G):
        return False

    if start is not None:
        visited = set()
        stack = [start]
        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            stack.extend(nx.eager.neighbors(G, curr))
        return len(visited) == nx.number_of_nodes(G)

    else:
        return nx.is_connected(G) and nx.eulerian_path(G) is not None
