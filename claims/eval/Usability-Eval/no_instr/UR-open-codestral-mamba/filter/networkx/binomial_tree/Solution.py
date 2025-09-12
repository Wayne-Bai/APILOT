import networkx as nx

def create_binomial_tree(n):
    # Create an empty graph
    G = nx.Graph()

    # Add the root node
    G.add_node(0)

    # Create the tree in a breadth-first manner
    queue = [0]

    while queue:
        # Get the next node
        node = queue.pop(0)

        # If the node is already on the last level, skip it
        if len(G[node]) < n:
            # Add its children and add them to the queue
            for i in range(len(G[node]), n):
                G.add_edge(node, node*(10 if i > 0 else 1)+i)
                queue.append(node*(10 if i > 0 else 1)+i)

    return G

# Create a binomial tree of order 3
binomial_tree = create_binomial_tree(3)

# Print the tree
nx.draw(binomial_tree, with_labels=True)
nx.draw_networkx_nodes(binomial_tree, nodelist=[0], node_color='r')

# Show the image
nx.show()
