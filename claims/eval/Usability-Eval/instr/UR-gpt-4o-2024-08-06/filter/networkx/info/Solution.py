import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (2, 4)])

# Function to print summary for the entire graph G
def print_graph_summary(graph):
    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()
    density = nx.density(graph)
    print("Graph Summary:")
    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")
    print(f"Density: {density:.4f}")

# Function to print summary for a specific node n
def print_node_summary(graph, node):
    if graph.has_node(node):
        degree = graph.degree(node)
        neighbors = list(graph.neighbors(node))
        print(f"Node {node} Summary:")
        print(f"Degree: {degree}")
        print(f"Neighbors: {neighbors}")
    else:
        print(f"Node {node} does not exist in the graph.")

# Call the functions to print summaries
print_graph_summary(G)
print_node_summary(G, 1)
