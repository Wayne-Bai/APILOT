import networkx as nx
import matplotlib.pyplot as plt
import random

def barabasi_albert_graph(n, m):
    G = nx.create_empty_graph(m)
    G.name="Barabasi-Albert Graph"

    # List of nodes to represent the preferential attachment process    
    target_nodes = list(range(m))
    # Start adding the other n-m nodes. The first node is added to the first m nodes and subsequent nodes are added with preferential attachment.
    source = m
    while source < n:
        G.add_edges_from(zip([source]*m, target_nodes))
        # Preferential attachment: The more connected a node is, the more likely it is to receive new links    
        target_nodes = list(reversed(sorted(target_nodes, key=lambda x: G.degree(x))))
        target_nodes = target_nodes[:m]
        target_nodes.append(source)
        source += 1

    return G

# Create barabasi_albert_graph with 50 nodes and 2 initial edges.
G = barabasi_albert_graph(50, 2)

# Print graph information
print("Nodes: ", G.number_of_nodes())
print("Edges: ", G.number_of_edges())
print("Degree centrality:", nx.degree_centrality(G))

# Draw the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
nx.draw_networkx_edges(G, pos, width=2, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
plt.show()
