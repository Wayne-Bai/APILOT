
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Define a function to consume an iterator and perform a BFS on the graph
def consume_iterator(iter):
    visited = set()
    for node in iter:
        if node not in visited:
            visited.add(node)
            G.bfs(node, depth_limit=2)
    return visited

# Create an iterator over the nodes in the graph
nodes = G.nodes()

# Consume the iterator and perform a BFS on the graph
visited = consume_iterator(nodes)

print("Visited nodes:", visited)
