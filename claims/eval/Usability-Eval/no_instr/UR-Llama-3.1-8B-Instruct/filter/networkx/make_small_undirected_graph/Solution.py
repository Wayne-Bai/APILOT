import networkx as nx

def create_graph(graph_description):
    # Create an empty graph
    G = nx.Graph()

    # Iterate over each key-value pair in the graph description
    for node, neighbors in graph_description.items():
        # Add the node to the graph
        G.add_node(node)
        
        # Iterate over each neighbor of the current node
        for neighbor in neighbors:
            # Add the edge between the current node and its neighbor
            G.add_edge(node, neighbor)
            
    return G

# Example usage
graph_description = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

G = create_graph(graph_description)

# Print graph properties
print("Nodes:", list(G.nodes))
print("Edges:", list(G.edges))

# Print graph adjacency list
print("Adjacency List:")
for node in G.nodes:
    print(f"{node}: {list(G.neighbors(node))}")

# G.set_node_attributes({'color': ['red', 'blue', 'green','red', 'blue', 'green']}, 'color')
