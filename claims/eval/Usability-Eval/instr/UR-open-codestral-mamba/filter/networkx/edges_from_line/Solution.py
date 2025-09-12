import networkx as nx

def generate_edges(geom):
    G = nx.Graph()

    # Add edges based on the line geometry
    for i in range(len(geom) - 1):
        start = geom[i]
        end = geom[i + 1]
        G.add_edge(start, end)

    return G

# Example usage
geom = [(0, 0), (1, 1), (2, 2), (3, 3)]
G = generate_edges(geom)
print(G.edges())
