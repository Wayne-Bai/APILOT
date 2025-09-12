
import tensorflow as tf

# Example usage of the tf.nest public API functionalities
nested_tensors = {
    'first': tf.constant(1),
    'second': {
        'inner': tf.constant(2),
        'another_inner': tf.constant(3)
    }
}

# Flatten the nested structure
flat_tensors = tf.nest.flatten(nested_tensors)
print("Flattened Tensors:", flat_tensors)

# Pack the flat tensors into the original nested structure
reconstructed_tensors = tf.nest.pack_sequence_as(nested_tensors, flat_tensors)
print("Reconstructed Tensors:", reconstructed_tensors)

# Map a function to each tensor in the nested structure
def square_tensor(tensor):
    return tf.square(tensor)

mapped_tensors = tf.nest.map_structure(square_tensor, nested_tensors)
print("Mapped Tensors:", mapped_tensors)
