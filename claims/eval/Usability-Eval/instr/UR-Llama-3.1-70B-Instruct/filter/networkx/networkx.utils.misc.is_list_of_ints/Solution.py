import networkx as nx

def is_list_of_ints(lst):
    """
    Return True if lst is a list of ints.
    
    Parameters
    ----------
    lst : list
        Input list
    
    Returns
    -------
    bool
        Whether lst is a list of ints
    """
    return all(isinstance(item, int) for item in lst)

# Create an empty graph
G = nx.Graph()

# Example usage:
print(is_list_of_ints([1, 2, 3, 4, 5]))  # True
print(is_list_of_ints([1, 2, '3', 4, 5]))  # False
