
import networkx as nx

def generate_edges(geom):
    # Initialize an empty list to store the edges
    edges = []
    
    # Loop through each line in the geometry
    for line in geom:
        # Extract the starting and ending points of the line
        start, end = line[0], line[-1]
        
        # Add the edge to the list of edges
        edges.append((start, end))
    
    return edges
