# Import required modules
import networkx as nx
import matplotlib.pyplot as plt

# Define a function to create a binomial tree of order n
def binomial_tree(n):
    # Create a new directed graph
    G = nx.DiGraph()
    
    # Function to return the level of a node in the tree
    def node_level():
        level = 1
        for node in G.nodes:
            G.nodes[node]['level'] = level
            level += 1
    
    # Function to return the parent of a node in the tree
    def get_parent(node):
        prev_level = G.nodes[node]['level'] - 1
        for n in G.nodes:
            if G.nodes[n]['level'] == prev_level:
                for neighbor in G.neighbors(n):
                    if G.nodes[neighbor]['level'] == G.nodes[node]['level']:
                        return n
    
    # Add nodes to the graph
    for i in range(2**n):
        G.add_node(i)
        
    # Add edges between parents and children
    for i in range(2**n):
        if i % 2 == 0:
            parent = get_parent(i)
            G.add_edge(parent, i)
            if i % 2 == 0:
                G.add_edge(i, i + 1)
            else:
                G.add_edge(i + 1, i)
    
    # Position nodes based on level in the graph
    node_level()
    pos = nx.spring_layout(G)
    
    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color='lightblue')
    
    # Display the graph
    plt.show()

# Test the function with order 5
binomial_tree(5)
