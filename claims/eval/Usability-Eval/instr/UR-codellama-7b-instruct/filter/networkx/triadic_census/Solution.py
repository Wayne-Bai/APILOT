
from networkx import DiGraph

def triadic_census(G):
    # Create a dictionary to store the count of each type of triad
    triad_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0,
                   11: 0, 12: 0, 13: 0, 14: 0, 15: 0}

    # Iterate over the nodes in the graph
    for node in G.nodes:
        # Get the neighbors of the current node
        neighbors = [nbr for nbr in G[node]]

        # Iterate over the neighbors to find triads
        for neighbor in neighbors:
            # Get the next neighbor
            second_neighbor = [nbr for nbr in G[neighbor] if nbr not in neighbors][0]

            # Calculate the type of triad and increment the count
            triad_type = 1 if node <= neighbor else 2
            triad_type *= 3 if second_neighbor >= neighbor else 1
            triad_count[triad_type] += 1

    return triad_count
