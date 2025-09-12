import pickle
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes
G.add_node("A", attr_dict={"attr1": "value1", "attr2": "value2"})
G.add_node("B", attr_dict={"attr1": "value3", "attr2": "value4"})
G.add_node("C", attr_dict={"attr1": "value5", "attr2": "value6"})

# Add edges
G.add_edge("A", "B", weight=0.1)
G.add_edge("B", "C", weight=0.2)
G.add_edge("C", "A", weight=0.3)

# Save the graph as a pickle file
with open("graph.pickle", "wb") as f:
    pickle.dump(G, f)
