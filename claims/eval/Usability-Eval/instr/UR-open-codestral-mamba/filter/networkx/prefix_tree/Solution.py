import networkx as nx
from networkx.drawing.nx_agraph import to_agraph

def create_prefix_tree(paths):
    graph = nx.DiGraph()
    for path in paths:
        segments = path.split("/")
        if len(segments) > 0:
            source = ""
            for segment in segments:
                target = source + "/" + segment if source else segment
                if target not in graph:
                    graph.add_node(target)
                if source:
                    graph.add_edge(source, target)
                source = target
    return graph

# Example usage
paths = ["/home/user1", "/home/user2", "/home/user3", "/usr/bin", "/usr/lib"]
graph = create_prefix_tree(paths)
nx.draw(graph, with_labels=True)
