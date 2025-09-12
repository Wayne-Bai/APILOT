import networkx as nx

def generate_duplication_divergence_graph(n, m1, m2, p):
    # Create an empty graph
    G = nx.empty_graph(n)

    # Add m1+m2 edges
    for i in range(m1+m2):
        if i < m1:
            # Duplication: Preferential attachment
            G = nx.duplication_divergence_graph(n, p, m1=1, m2=0, seed=None)
        else:
            # Divergence: Preferential attachment
            G = nx.duplication_divergence_graph(n, p, m1=0, m2=1, seed=None)

    return G

# Test the function
G = generate_duplication_divergence_graph(100, 2, 2, 0.5)
print(G)
