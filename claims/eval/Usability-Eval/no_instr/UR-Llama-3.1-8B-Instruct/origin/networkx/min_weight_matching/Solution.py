import networkx as nx
import heapq

def min_weight_maximal_matching(G):
    """
    Compute the minimum-weight maximal matching of G.
    
    Parameters:
    G : networkx Graph
        The input graph.
    
    Returns:
    matching : dictionary
        A dictionary where matching[u] = v is the minimum-weight matching of u.
    """

    # Step 1: Assign weights to the edges of the graph
    for u, v in G.edges():
        G[u][v]['weight'] = 1  # assign a weight to each edge as 1 to avoid potential division by zero, actual weights should be provided/supplied in place of 1

    # Add dummy nodes and edges to connect them
    G.add_node('s')
    G.add_node('t')
    for u in G.nodes():
        G.add_edge('s', u, weight=0)
        G.add_edge(u, 't', weight=0)

    # Step 2: Run the maximum flow algorithm
    flow_value, flow_dict = nx.maximum_flow(G,'s', 't', flow_func=nx.edgelist_flow)

    # Remove dummy nodes and edges
    G.remove_node('s')
    G.remove_node('t')

    # Create an empty dictionary to store the matching
    matching = {}

    # Step 3: Find the minimum-weight maximal matching
    for u, v in flow_dict:
        # If the flow is greater than 0, add the edge to the matching
        if flow_dict[u, v] > 0:
            matching[u] = v

    return matching

# Example usage:
G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'D')
G.add_edge('C', 'D')

matching = min_weight_maximal_matching(G)
print(matching)
