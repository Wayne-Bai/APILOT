
import networkx as nx

# Create a simple directed graph
graph = nx.DiGraph()

# Add nodes and edges
graph.add_nodes_from(['A', 'B', 'C'])
graph.add_edges_from([('A', 'B'), ('B', 'C')])

# Define the graph description
graph_description = {'A': ['B'], 'B': ['C']}

# Return the small graph described by graph_description
return nx.induced_subgraph(graph, graph_description)
