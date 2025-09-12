import networkx as nx

# Define a list of paths
paths = [
    'A->B->C',
    'A->D',
    'A->E',
    'B->F',
    'E->G->H',
    'G->I'
]

# Create an empty directed graph
graph = nx.DiGraph()

# Add each path as a series of edges in order
for path in paths:
    nodes = path.split('->')
    for i in range(len(nodes) - 1):
        from_node = nodes[i]
        to_node = nodes[i + 1]
        graph.add_edge(from_node, to_node)

# Print the graph in the format A -> B -> C ...
for edge in graph.edges(data=True):
    from_node = edge[0]
    to_node = edge[1]
    print(f'{from_node} -> {to_node}')
