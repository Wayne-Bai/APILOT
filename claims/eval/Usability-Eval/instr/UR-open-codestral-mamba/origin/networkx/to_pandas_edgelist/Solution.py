import networkx as nx
import pandas as pd

# Create a graph
G = nx.Graph()

# Add edges
G.add_edge('A', 'B', weight=2)
G.add_edge('B', 'C', weight=4)
G.add_edge('C', 'D', weight=3)

# Get edge list
edge_list = G.edges(data=True)

# Convert edge list to pandas DataFrame
df_edge_list = pd.DataFrame(edge_list, columns=['Node_1', 'Node_2', 'Weight'])

# Print DataFrame
print(df_edge_list)
