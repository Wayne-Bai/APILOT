import networkx as nx

# Define the number of nodes and edges
num_nodes = 100
num_edges = 5

# Create an empty graph
G = nx.Graph()

# Add the initial node
G.add_node(1)

# Add the remaining nodes and edges
for i in range(2, num_nodes+1):
    # Add a node
    G.add_node(i)

    # Add edges based on the preferential attachment model
    for j in range(1, i):
        # Add an edge with probability proportional to the degree
        if nx.degree(G, j) > 0 and nx.random.uniform() < num_edges * float(nx.degree(G, j)) / (2 * G.number_of_edges()):
            G.add_edge(i, j)

# Check if the graph has the desired number of edges
while G.number_of_edges() < num_edges:
    # Choose two random nodes
    u, v = nx.random.choice(G.nodes(), 2)

    # If the nodes are not already connected, add an edge
    if not G.has_edge(u, v):
        G.add_edge(u, v)

# Print the generated graph
print(G.nodes())
print(G.edges())
