
import networkx as nx

def generate_edges(geom):
    G = nx.Graph()
    
    for line in geom:
        for i in range(len(line)-1):
            G.add_edge(line[i], line[i+1])
    
    return G
