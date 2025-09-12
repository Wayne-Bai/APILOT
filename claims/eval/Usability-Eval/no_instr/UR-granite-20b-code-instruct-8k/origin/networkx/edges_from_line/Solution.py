import networkx as nx

def generate_edges(geom):
    # Create a graph
    G = nx.Graph()

    # Loop through each line in geom
    for line in geom:
        # Get the coordinates of the line
        coords = list(line.coords)

        # Add the coordinates as nodes to the graph
        for i in range(len(coords) - 1):
            G.add_node(coords[i])
            G.add_node(coords[i+1])

        # Add edges to the graph
        for i in range(len(coords) - 1):
            G.add_edge(coords[i], coords[i+1])

    return G
