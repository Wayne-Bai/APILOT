# Import networkx library
import networkx as nx

# Create an empty graph
G = nx.Graph()

# Create a function to generate a unique node label
def generate_unique_node_label(G):
    """
    Generate a unique node label for the given graph.
    
    Args:
    G (networkx Graph): The input graph.
    
    Returns:
    str: A unique node label.
    """
    
    # Get the list of existing node labels
    existing_labels = list(G.nodes())
    
    # Initialize a counter to generate unique labels
    counter = 0
    
    # Loop until a unique label is generated
    while True:
        # Generate a potential label
        potential_label = f"node_{counter}"
        
        # Check if the potential label is unique
        if potential_label not in existing_labels:
            # Return the unique label
            return potential_label
        
        # Increment the counter for the next iteration
        counter += 1

# Test the function by adding a new node with a unique label
unique_label = generate_unique_node_label(G)
G.add_node(unique_label)

# Print the nodes in the graph to verify the unique label
print("Nodes in the graph:", list(G.nodes()))
