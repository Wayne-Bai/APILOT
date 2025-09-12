import yaml
import networkx as nx

# Create a graph using NetworkX
G = nx.Graph()

# Add edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (4, 5), (5, 1)])

# Convert graph to YAML format
def gen_graph_app_node_formats(graph):
    nodes = {}
    for node in graph.nodes():
        nodes[node] = {"id": node}

    edges = {}
    for edge in graph.edges():
        edges[edge] = {"source": edge[0], "target": edge[1]}

    return {"nodes": nodes, "edges": edges}

graph_in_yaml = gen_graph_app_node_formats(G)

# Write to YAML file
with open('graph.yaml', 'w') as file:
    yaml.safe_dump(graph_in_yaml, file)
