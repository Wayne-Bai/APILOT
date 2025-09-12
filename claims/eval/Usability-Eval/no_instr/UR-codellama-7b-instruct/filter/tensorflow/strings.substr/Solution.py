import tensorflow as tf

# Define a function that takes in a tensor of strings and returns a list of substrings
def get_substrings(tensor):
    # Use the tf.string_split() operation to split each string in the tensor into a list of substrings
    substrings = tf.map_fn(lambda s: tf.string_split([s], [' ']), tensor)
    # Flatten the nested lists of substrings into a single list
    flattened = tf.keras.backend.flatten(substrings)
    return flattened
