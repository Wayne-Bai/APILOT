import networkx as nx

def hits_algorithm(graph):
    H = dict.fromkeys(graph.nodes, 0)
    A = dict.fromkeys(graph.nodes, 0)

    for node in graph.nodes():
        for neighbor in graph.neighbors(node):
            A[neighbor] += 1
            H[node] += 1

    for k in range(20):
        H_new = dict.fromkeys(graph.nodes(), 0)
        A_new = dict.fromkeys(graph.nodes(), 0)

        for v in graph.nodes():
            for w in graph.neighbors(v):
                H_new[v] += ((A[w] * H[w]) ** 0.5) / A[w]

            for w in graph.neighbors(v):
                A_new[w] += ((H[v] * ((A[w] ** 0.5) / A[v])) ** 0.5) / (H[v] ** 0.5)

        H = H_new
        A = A_new

    return H

# Example usage with a simple graph
if __name__ == "__main__":
    G = nx.erdos_renyi_graph(10, 0.1)  # Create a random graph with 10 nodes and 0.1 edge probability
    hits_matrix = hits_algorithm(G)
    print("HITS Authority Matrix:", hits_matrix)
