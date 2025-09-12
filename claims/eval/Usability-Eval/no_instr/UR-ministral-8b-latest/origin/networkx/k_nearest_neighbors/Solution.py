import networkx as nx

# Function to compute the average degree connectivity of a graph
def average_degree_connectivity(G, k):
    degree = dict(G.degree())
    average_degree = 0.0
    count = 0.0

    for node in G.nodes():
        if degree[node] == k:
            for neighbor in G.neighbors(node):
                if degree[neighbor] in degree.values():
                    average_degree += degree[neighbor]
                    count += 1

    if count > 0:
        return average_degree / count
    else:
        return 0

# Example usage
G = nx.erdos_renyi_graph(100, 0.1)
k = 4

average_degree_conn = average_degree_connectivity(G, k)
print(f"Average degree connectivity for degree {k}: {average_degree_conn}")
