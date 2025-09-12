import networkx as nx

def is_list_of_ints(lst):
    return all(isinstance(i, int) for i in lst)

# Example usage:
G = nx.Graph()
nodes = [1, 2, 3, 4, 5]
G.add_nodes_from(nodes)

print(is_list_of_ints(nodes))  # Returns: True
