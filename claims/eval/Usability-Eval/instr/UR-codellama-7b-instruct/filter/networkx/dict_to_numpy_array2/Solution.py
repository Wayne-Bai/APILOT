
import networkx as nx

# Define the dictionary of dictionaries
data = {
    "node1": {"weight": 0.5, "color": "red"},
    "node2": {"weight": 0.8, "color": "blue"},
    "node3": {"weight": 0.3, "color": "green"}
}

# Convert the dictionary of dictionaries to a 2d numpy array with optional mapping
matrix = nx.to_numpy_array(data)
print(matrix)
