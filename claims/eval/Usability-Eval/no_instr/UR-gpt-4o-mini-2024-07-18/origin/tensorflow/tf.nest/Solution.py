import tensorflow as tf

# Example usage of tf.nest to demonstrate its functionality

# Creating a nested structure of TensorFlow elements
nested_structure = {
    'a': tf.constant(1),
    'b': [tf.constant(2), tf.constant(3)],
    'c': {
        'd': tf.constant(4),
        'e': [tf.constant(5), tf.constant(6)]
    }
}

# Function to flatten the nested structure
flat_list = tf.nest.flatten(nested_structure)

print("Flattened list of tensors:")
for tensor in flat_list:
    print(tensor.numpy())
