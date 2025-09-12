import networkx as nx

def is_list_of_ints(lst):
    """ Returns True if the given list contains only integers, else returns False. """
    return all(isinstance(item, int) for item in lst)

# Example usage:
example_list = [1, 2, 3, 4]
print(is_list_of_ints(example_list))  # Output: True

another_list = [1, 'a', 3.5]
print(is_list_of_ints(another_list))  # Output: False
