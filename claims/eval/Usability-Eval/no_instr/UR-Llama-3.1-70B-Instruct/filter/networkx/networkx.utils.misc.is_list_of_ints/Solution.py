import networkx as nx

def is_list_of_ints(lst):
    """
    Return True if list is a list of ints.
    
    Parameters
    ----------
    lst : list
        The input list.
    
    Returns
    -------
    bool
        Whether the list only contains integers.
    """
    return all(isinstance(i, int) for i in lst)

# Example usage:
G = nx.Graph()
numbers = [1, 2, 3, 4, 5]
not_numbers = ['a', 2, 3, 4, 5]

print(is_list_of_ints(numbers))  # Output: True
print(is_list_of_ints(not_numbers))  # Output: False
