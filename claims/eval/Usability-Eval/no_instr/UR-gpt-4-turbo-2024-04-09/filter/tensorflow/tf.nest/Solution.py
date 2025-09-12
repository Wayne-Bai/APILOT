import tensorflow as tf

# Example function to demonstrate usage of tf.nest methods

def nest_example():
    # Define nested structures
    nested_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    nested_dict = {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}}
    
    # Flatten nested structures
    flat_list = tf.nest.flatten(nested_list)
    flat_dict = tf.nest.flatten(nested_dict)
    
    print("Flattened list:", flat_list)
    print("Flattened dict:", flat_dict)
    
    # Map a function to each element in the nested structure
    squared_list = tf.nest.map_structure(lambda x: x**2, nested_list)
    squared_dict = tf.nest.map_structure(lambda x: x**2, nested_dict)

    print("Squared list:", squared_list)
    print("Squared dict:", squared_dict)

    # Check if two structures are nested in the same way
    is_same_structure = tf.nest.is_nested(nested_list)
    print("Is nested_list a nested structure?", is_same_structure)

# Run the example
nest_example()
