import networkx as nx
import yaml

def read_graph_from_yaml(file_path):
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
        G = nx.MultiGraph()
        for node in data:
            G.add_node(node)
        for edge in data:
            for neighbor in data[edge]:
                G.add_edge(edge, neighbor)
    return G

def write_graph_to_yaml(G, file_path):
    with open(file_path, "w") as file:
        yaml.dump(graph_to_dict(G), file, default_flow_style=False)

def graph_to_dict(G):
    graph_dict = {}
    for node in G.nodes(data=True):
        if node[0] not in graph_dict:
            graph_dict[node[0]] = {}
        graph_dict[node[0]]["attributes"] = node[1]
    for edge in G.edges(data=True):
        if edge[0] not in graph_dict:
            graph_dict[edge[0]] = {}
        if edge[2]:
            graph_dict[edge[0]]["attributes"] = edge[2] if "attributes" not in graph_dict[edge[0]] else {**graph_dict[edge[0]]["attributes"], **edge[2]}
        graph_dict[edge[0]][edge[1]] = "edge"
    for node in G.nodes():
        if node not in graph_dict and len(G.neighbors(node)) == 0:
            graph_dict[node] = {}
    return graph_dict

# Example Usage:
G = nx.Graph()
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "C")
write_graph_to_yaml(G, "graph.yaml")
read_from_yaml = read_graph_from_yaml("graph.yaml")
