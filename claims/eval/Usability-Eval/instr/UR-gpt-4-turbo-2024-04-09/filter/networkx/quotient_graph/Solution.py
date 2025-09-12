import networkx as nx

def equivalence_relation(u, v):
    # Define your own equivalence relation here.
    # This is a simple example where nodes are equivalent if they have the same remainder when divided by 2
    return u % 2 == v % 2

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (2, 5)])

# Compute the quotient graph based on the defined equivalence relation
Q = nx.quotient_graph(G, equivalence_relation)

# Print the edges of the quotient graph
print("Nodes in the Quotient Graph:")
print(Q.nodes())
print("Edges in the Quotient Graph:")
print(Q.edges())
