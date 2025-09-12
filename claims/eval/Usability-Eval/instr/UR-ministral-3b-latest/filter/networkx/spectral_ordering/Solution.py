import networkx as nx

g = nx.karate_club_graph()

# Find the largest weakly connected component
lcc = max(nx.weakly_connected_components(g), key=len)

# Compute the spectral assignment
def spectral_ordering(lcc):
    G = g.subgraph(lcc).copy()
    H = nx.laplacian_matrix(G).toarray()
    E, V = H.shape
    D = dict()
    for i in range(E):
        H_n_i = H[i]
        for j in range(V):
            if H_n_i[j] != 0:
                D[i] = j

    lambdas = sorted(nx.laplacian_similarity_matrix(G, norm='2').eigenvecs()[1][:, 1])
    ordering = [v for v in sorted(map(D.get, range(E)))][::-1]  # sort by eigenvalues
    return [g.nodes[i][0] for i in ordering]

ordering = list(spectral_ordering(lcc))
