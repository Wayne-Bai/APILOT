# Import the necessary libraries
import networkx as nx
import pickle

# Create a new directed graph
G = nx.DiGraph()

# Add nodes to the graph
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")

# Add edges to the graph
G.add_edge("A", "B")
G.add_edge("B", "D")
G.add_edge("C", "B")
G.add_edge("C", "D")
G.add_edge("D", "E")

# Write the graph in Python pickle format
with open("graph.pkl", "wb") as f:
    pickle.dump(G, f)

print("Graph written to graph.pkl")
