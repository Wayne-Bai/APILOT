import networkx as nx
import pandas as pd

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')

# Add edges to the graph
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')
G.add_edge('D', 'A')
G.add_edge('A', 'C')

# Convert the graph to a Pandas DataFrame
df = pd.DataFrame(list(G.edges), columns=['Source', 'Destination'])

# Print the edge list as a Pandas DataFrame
print(df)
