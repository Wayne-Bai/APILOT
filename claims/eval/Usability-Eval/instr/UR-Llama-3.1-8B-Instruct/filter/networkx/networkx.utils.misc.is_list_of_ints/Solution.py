import networkx as nx

def is_list_of_ints(lst):
    """
    Returns True if lst is a list of ints, False otherwise.
    
    :param lst: The list to check.
    :return: Boolean indicating if the list is a list of ints.
    """
    try:
        return all(isinstance(x, int) for x in lst)
    except AttributeError:
        return False

# Test cases
print(is_list_of_ints([1, 2, 3]))  # Expected output: True
print(is_list_of_ints([1, 'a', 3]))  # Expected output: False
print(is_list_of_ints([1, 2, 'three']))  # Expected output: False

# Using networkx (not necessary for this case, but included as per requirement)
# You can use the isinstance() function from Python's built-in types module instead of networkx
# networkx is typically used for graph operations, not for type checking
# But if you want to use networkx for some other purpose, you can, else comment this block out
print(nx.__version__)  # If you want to check if networkx is imported correctly
