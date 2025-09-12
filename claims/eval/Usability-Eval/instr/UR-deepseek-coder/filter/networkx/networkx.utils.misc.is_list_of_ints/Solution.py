import networkx as nx

def is_list_of_ints(lst):
    return all(isinstance(item, int) for item in lst)

# Example usage:
# print(is_list_of_ints([1, 2, 3]))  # Should return True
# print(is_list_of_ints([1, '2', 3]))  # Should return False
