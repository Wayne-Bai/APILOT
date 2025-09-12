""
import networkx as nx

# Function to read data from JIT JSON and create a NetworkX graph
def create_graph_from_jit_json(json_data):
    G = nx.Graph()
    for item in json_data:
        node_id = item['id']
        node_data = item['data']
        G.add_node(node_id, attr_dict=node_data)

    for item in json_data:
        source_id = item['id']
        targets = item.get('targets', [])
        for target in targets:
            target_id = target['id']
            edge_data = target.get('data', {})
            G.add_edge(source_id, target_id, attr_dict=edge_data)
    return G

# Sample JIT JSON data (Replace with actual data)
sample_json_data = [
    {
        "id": "1",
        "data": {
            "label": "Node 1"
        },
        "targets": [
            {
                "id": "2",
                "data": {
                    "label": "Node 2"
                }
            },
            {
                "id": "3",
                "data": {
                    "label": "Node 3"
                }
            }
        ]
    },
    {
        "id": "2",
        "data": {
            "label": "Node 2"
        }
    },
    {
        "id": "3",
        "data": {
            "label": "Node 3"
        }
    }
]

G = create_graph_from_jit_json(sample_json_data)

# Print graph information
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
""
