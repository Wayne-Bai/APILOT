import networkx as nx

def is_list_of_ints(input_list):
    for item in input_list:
        if not isinstance(item, int):
            return False
    return True

# Test cases
print(is_list_of_ints([1, 2, 3, 4]))  # True
print(is_list_of_ints([1, "2", 3]))    # False
print(is_list_of_ints([1.0, 2.0]))     # False (considering floats)
print(is_list_of_ints([]))            # True
