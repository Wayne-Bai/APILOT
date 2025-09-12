import networkx as nx

def is_list_of_ints(input_list):
    return all(isinstance(i, int) for i in input_list)

# Example usage:
numbers = [1, 2, 3, 4, 5]
print(is_list_of_ints(numbers))
