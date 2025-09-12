import numpy as np
from scipy.sparse import csr_matrix, Diagonal
from scipy.sparse.linalg import egv

def construct_laplacian_string(graph, directed=True):
    if directed:
        degree_sequence = np.zeros(len(graph), dtype=int)
        diagonal = np.diag(len(graph))

        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i, j] != 0:  # Update if there is an edge
                    diagonal[i] += 1
                    degree_sequence[i, j] = 1
                    diagonal[j] += 1
                    degree_sequence[j, i] = 1
    else:
        geographic = (np.eye(len(graph))
                      - np.diag(np.array(degree_sequence)))
        row = np.array(geographic).T
        col = np.array(geographic)
        data = -row * np.diag(np.array(degree_sequence))
    return Diagonal(diagonal).toarray()

graph = np.array([[0,1,0], [1,0,1], [0,1,0]])
print(construct_laplacian_string(graph, directed=True))
