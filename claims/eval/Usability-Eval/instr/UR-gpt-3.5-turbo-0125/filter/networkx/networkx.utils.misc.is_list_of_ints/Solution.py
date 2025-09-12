
import networkx as nx

def is_list_of_ints(lst):
    return all(isinstance(elem, int) for elem in lst)

# Test the function
lst1 = [1, 2, 3, 4]
lst2 = [1, 2, 'a', 4]
print(is_list_of_ints(lst1))  # Output: True
print(is_list_of_ints(lst2))  # Output: False
