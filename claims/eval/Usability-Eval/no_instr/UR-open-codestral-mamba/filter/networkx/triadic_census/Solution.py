import networkx as nx

def triadic_census(G, nodelist=None):
    # Initialize a dictionary to store the count of each triad type
    triad_counts = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0}

    # Get the list of nodes in the graph
    nodes = G.nodes()

    # If a nodelist is provided, only consider triads that includes nodes from the nodelist
    if nodelist is not None:
        nodes = [node for node in nodes if node in nodelist]

    # Iterate over all possible triads in the graph
    for u in nodes:
        for v in nodes:
            for w in nodes:
                # Skip triads that have less than 3 nodes or have nodes in common
                if u == v or u == w or v == w:
                    continue
                # Determine the triad type based on the adjacency between the nodes
                if G.has_edge(u, v) and G.has_edge(v, w) and G.has_edge(w, u):
                    triad_type = 1
                elif G.has_edge(u, v) and G.has_edge(v, w):
                    triad_type = 2
                elif G.has_edge(v, w) and G.has_edge(w, u):
                    triad_type = 3
                elif G.has_edge(u, v):
                    triad_type = 4
                elif G.has_edge(v, w):
                    triad_type = 5
                elif G.has_edge(w, u):
                    triad_type = 6
                elif G.has_edge(u, w):
                    triad_type = 7
                else:
                    triad_type = 8
                # Increment the count for the triad type
                triad_counts[triad_type] += 1
    return triad_counts
# Example usage
G = nx.DiGraph()
G.add_edges_from([(1,2), (2,3), (3,1)])
nodelist = [1, 2, 3]
triad_counts = triadic_census(G, nodelist)
print(triad_counts)
