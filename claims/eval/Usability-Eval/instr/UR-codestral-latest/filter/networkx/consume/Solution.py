import networkx as nx

# Assuming 'graph' is a pre-existing networkx graph object and 'iterator' is the iterator you're referring to

# If 'iterator' is an object of nodes
for node in iterator:
    # Consume the iterator entirely
    if node in graph:
        print(f'Node {node} is in the graph')
    else:
        print(f'Node {node} is not in the graph')

# If 'iterator' is an object of edges
for edge in iterator:
    # Consume the iterator entirely
    if edge in graph.edges():
        print(f'Edge {edge} is in the graph')
    else:
        print(f'Edge {edge} is not in the graph')
