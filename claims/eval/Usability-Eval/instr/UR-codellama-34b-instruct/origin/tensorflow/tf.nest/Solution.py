
# Create a nested structure with multiple levels
nested_list = [1, 2, [3, 4], [[5]]]

# Flatten the nested list to a single level
flattened_list = nest.flatten(nested_list)
print(flattened_list)  # Output: [1, 2, 3, 4, 5]

# Map a function to each element of the nested list
def add_one(x):
    return x + 1
mapped_list = nest.map_structure(add_one, nested_list)
print(mapped_list)  # Output: [2, 3, [4], [[6]]]

# Apply a function to each element of the nested list and return a new structure
def multiply_by_two(x):
    return x * 2
new_nested_list = nest.apply_structure(multiply_by_two, nested_list)
print(new_nested_list)  # Output: [2, 4, [6], [[10]]]
