import networkx as nx

def equivalence_relation(n):
    # Define your equivalence relation
    # Here, for example, grouping nodes by even or odd values
    return n % 2

def create_quotient_graph(G):
    # Partition of the graph's nodes based on the equivalence relation
    partition = []
    node_group = {}

    for node in G.nodes():
        group_id = equivalence_relation(node)
        if group_id not in node_group:
            node_group[group_id] = []
        node_group[group_id].append(node)

    for group in node_group.values():
        partition.append(group)

    # Creating the quotient graph
    Q = nx.quotient_graph(G, partition)
    return Q

# Example usage
G = nx.cycle_graph(6)  # Create a cycle graph C6
Q = create_quotient_graph(G)
print("Quotient Graph Nodes:", Q.nodes(data=True))
print("Quotient Graph Edges:", Q.edges(data=True))
