import networkx as nx

def create_graph(graph_description):
    # Create an empty graph
    G = nx.Graph()

    # Add nodes and edges based on the graph description
    nodes_and_edges = graph_description.split(" ")
    for i in range(0, len(nodes_and_edges), 2):
        node = nodes_and_edges[i]
        neighbors = nodes_and_edges[i+1].split(",")
        G.add_node(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    return G

# Graph description
graph_description = "A B,C D E F G H I"

# Create the graph
graph = create_graph(graph_description)

# Display the graph
nx.draw(graph, with_labels=True)
