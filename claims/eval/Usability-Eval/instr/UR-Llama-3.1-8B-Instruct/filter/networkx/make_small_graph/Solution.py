import networkx as nx

# Define the graph description
graph_description = {
    "nodes": ["A", "B", "C", "D"],
    "edges": [
        {"source": "A", "target": "B", "weight": 1},
        {"source": "B", "target": "C", "weight": 1},
        {"source": "C", "target": "D", "weight": 1},
        {"source": "D", "target": "B", "weight": 1},
        {"source": "A", "target": "C", "weight": 2},
        {"source": "B", "target": "D", "weight": 3},
    ]
}

# Create a new directed graph
G = nx.DiGraph()

# Add nodes to the graph
for node in graph_description["nodes"]:
    G.add_node(node)

# Add edges to the graph
for edge in graph_description["edges"]:
    G.add_edge(edge["source"], edge["target"], weight=edge["weight"])

print("Graph Nodes:", list(G.nodes))
print("Graph Edges:", dict(G.edges(data=True)))
