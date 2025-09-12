# Import necessary libraries
import networkx as nx
import matplotlib.pyplot as plt

# Function to calculate PageRank
def calculate_page_rank(graph):
    """
    Calculate the PageRank of each node in the graph.

    Parameters:
    graph (nx.Graph): The graph to calculate PageRank for.

    Returns:
    dict: A dictionary where the keys are the node IDs and the values are the PageRank scores.
    """
    # Remove isolated nodes: PageRank is only defined for nodes with at least one incoming link
    graph.remove_nodes_from(list(nx.isolates(graph)))
    
    # Calculate PageRank
    try:
        ranks = nx.pagerank(graph, weight='weight')
    except nx.NetworkXError:
        # If there are no edges in the graph, calculate PageRank on the unweighted graph instead
        ranks = nx.pagerank(graph)
        
    return ranks

# Create a simple directed graph
G = nx.DiGraph()

# Add nodes
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')

# Add edges
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=1)
G.add_edge('B', 'D', weight=1)
G.add_edge('C', 'D', weight=2)

# Calculate PageRank
ranks = calculate_page_rank(G)

# Print the PageRank scores
print("PageRank scores:")
for node, score in ranks.items():
    print(f"{node}: {score:.4f}")

# Visualize the graph with PageRank scores
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=[200 * (score + 1) for score in ranks.values()])
nx.draw_networkx_labels(G, pos, font_size=10)
nx.draw_networkx_edges(G, pos)
plt.show()
