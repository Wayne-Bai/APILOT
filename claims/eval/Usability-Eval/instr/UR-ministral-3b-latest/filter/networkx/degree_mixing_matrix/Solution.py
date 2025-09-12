import networkx as nx

# Sample graph creation
G = nx.Graph()

# Add nodes
G.add_node('A')
G.add_node('B')
G.add_node('C')

# Add edges and attributes
G.add_edge('A', 'B', weight=0.5)
G.add_edge('A', 'C', weight=0.3)
G.add_edge('B', 'C', weight=0.2)

# Function to return mixing matrix for attributes
def mixing_matrix(G):
    mixing_matrix = {}
    for edge in G.edges(data=True):
        if 'weight' not in mixing_matrix:
            mixing_matrix['weight'] = []
        if edge[0] not in mixing_matrix:
            mixing_matrix[edge[0]] = {}
            if edge[1] not in mixing_matrix[edge[0]]:
                mixing_matrix[edge[0]][edge[1]] = {}
        for key, value in edge[2].items():
            if key not in mixing_matrix[edge[0]][edge[1]]:
                mixing_matrix[edge[0]][edge[1]][key] = [value]
            else:
                mixing_matrix[edge[0]][edge[1]][key].append(value)

    return mixing_matrix

# Return mixing matrix
print(mixing_matrix(G))
