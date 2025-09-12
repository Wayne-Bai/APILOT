import networkx as nx

def return_small_graph(graph_description):
    G = nx.Graph()
    
    # Check the type of graph description
    if type(graph_description) == dict:
        # If the description is a dictionary, assume it has nodes and edges keys
        if 'nodes' in graph_description and 'edges' in graph_description:
            G.add_nodes_from(graph_description['nodes'])
            G.add_edges_from(graph_description['edges'])
        else:
            raise ValueError("Invalid graph description dictionary. It should have 'nodes' and 'edges' keys.")
    elif type(graph_description) == list:
        # If the description is a list, assume each item is a list or tuple with two nodes
        G.add_edges_from(graph_description)
    elif graph_description == 'cycle_graph':
        # Return the Petersen graph
        return nx.cycle_graph(5)
    elif graph_description == 'cube_graph':
        # Return the cubic graph
        return nx.cubical_graph()
    # Add more specific graph descriptions if needed
    else:
        raise ValueError("Invalid graph description.")
        
    return G

## Usage:
graph_description = {
    'nodes': [1, 2, 3, 4, 5],
    'edges': [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
}

print(return_small_graph(graph_description).edges)
