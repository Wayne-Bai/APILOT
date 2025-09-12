import networkx as nx
import matplotlib.pyplot as plt

def compute_min_weight_maximal_matching(G):
    # Initialize an empty graph to store the matching
    matching = nx.Graph()
    matching.add_nodes_from(G.nodes)
    
    # Sort the edges by weight in ascending order
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    
    # Iterate over the sorted edges
    for u, v, weight in sorted_edges:
        # If the edge does not form a cycle and both nodes do not already have a match
        if not matching.has_edge(u, v) and not any(matching.has_edge(u, w) for w in matching.neighbors(v)) and not any(matching.has_edge(x, v) for x in matching.neighbors(u)):
            # Add the edge to the matching
            matching.add_edge(u, v, weight=weight)
    
    return matching

# Create a weighted graph
G = nx.Graph()
G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('C', 'D', weight=1)
G.add_edge('D', 'A', weight=3)
G.add_edge('A', 'C', weight=4)
G.add_edge('B', 'D', weight=5)

# Compute a minimum-weight maximal matching
matching = compute_min_weight_maximal_matching(G)

# Print the matching
print("Minimum-weight maximal matching:")
print(list(matching.edges(data=True)))

# Draw the graph
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()

# Draw the matching
pos = nx.spring_layout(matching)
nx.draw_networkx(matching, pos)
labels = nx.get_edge_attributes(matching,'weight')
nx.draw_networkx_edge_labels(matching,pos,edge_labels=labels)
plt.show()
