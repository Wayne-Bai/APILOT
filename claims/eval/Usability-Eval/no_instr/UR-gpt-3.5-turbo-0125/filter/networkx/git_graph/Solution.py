
import networkx as nx

jit_json_file = "graph.json"
with open(jit_json_file, "r") as f:
    data = json.load(f)

G = nx.Graph()

for node in data['nodes']:
    G.add_node(node['id'])

for edge in data['edges']:
    G.add_edge(edge['source'], edge['target'])

print(nx.info(G))
