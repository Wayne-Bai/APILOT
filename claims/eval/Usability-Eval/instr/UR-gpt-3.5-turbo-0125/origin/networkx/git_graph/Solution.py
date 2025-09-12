
import networkx as nx

# Read a graph from JIT JSON
def read_graph_from_JIT_JSON(json_data):
    G = nx.node_link_graph(json_data)
    return G

# Example usage
json_data = {"nodes": [{"id": 1, "group": 1}, {"id": 2, "group": 2}], "links": [{"source": 1, "target": 2}]}
graph = read_graph_from_JIT_JSON(json_data)
print(graph.nodes)
print(graph.edges)
