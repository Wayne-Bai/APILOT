
import networkx as nx

# Define the graph G
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 4)])

# Define the equivalence relation on nodes
def equivalent(u, v):
    return u == v or u + 1 == v or u - 1 == v

# Calculate the quotient graph of G under the equivalence relation
Q = nx.quotient_graph(G, equivalent)

# Print the quotient graph
print("Quotient graph:", Q)
