import tensorflow as tf

# Example function using tf._api.v2.nest
def nest_example(input_tensor):
    # Define a nested function
    def nested_function(x):
        return tf.math.add(x, 1)

    # Use tf._api.v2.nest within a wrapping function for demonstration purposes
    return tf.nest.map_structure(nested_function, input_tensor)
