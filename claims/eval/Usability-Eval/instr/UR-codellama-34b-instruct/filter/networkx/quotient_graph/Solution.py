
import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Define an equivalence relation on nodes
def node_eq(n1, n2):
    return n1 % 2 == n2 % 2

# Compute the quotient graph
Q = nx.quotient_graph(G, node_eq)

print("Nodes in Q:", Q.nodes())
print("Edges in Q:", Q.edges())
