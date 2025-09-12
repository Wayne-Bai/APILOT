
import networkx as nx

def subgraph_communicability_matrix(G):
    n = len(G)
    A = nx.adjacency_matrix(G).todense()  # Adjacency matrix of G
    I = np.eye(n)  # Identity matrix of size n

    A2 = A * A
    A3 = A2 * A
    S = np.linalg.inv(I - 0.5*A + (A2/12) - (A3/720))

    return S
