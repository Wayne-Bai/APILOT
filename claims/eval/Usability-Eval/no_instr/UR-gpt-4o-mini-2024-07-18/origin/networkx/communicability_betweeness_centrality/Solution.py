import networkx as nx

def subgraph_communicability(G):
    # Create a dictionary to hold the communicability for each pair of nodes
    communicability_dict = {}
    
    # Access all pairs of nodes in the graph
    for u in G.nodes():
        for v in G.nodes():
            if u != v:  # Avoid self-loops
                # Calculate the subgraph communicability between nodes u and v
                communicability = nx.communicability_between(G, u, v)
                communicability_dict[(u, v)] = communicability
                
    return communicability_dict

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (1, 3), (2, 3)])
# result = subgraph_communicability(G)
# print(result)
