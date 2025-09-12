import networkx as nx

def consume_iterator(iterator):
    for item in iterator:
        # Process the item here
        pass

# Create a graph
G = nx.Graph()

# Add nodes and edges
G.add_node("Node 1")
G.add_node("Node 2")
G.add_edge("Node 1", "Node 2")

# Get the iterator of nodes
node_iterator = G.nodes()

# Consume the iterator entirely
consume_iterator(node_iterator)
