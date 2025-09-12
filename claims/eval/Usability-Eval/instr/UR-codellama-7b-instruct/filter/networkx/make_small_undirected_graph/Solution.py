
import networkx as nx

# Define the graph description
graph_description = {
    'nodes': ['A', 'B', 'C', 'D'],
    'edges': [['A', 'B'], ['B', 'C'], ['C', 'D']]
}

# Create a small undirected graph using the networkx package
G = nx.Graph(graph_description)
