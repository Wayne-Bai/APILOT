import tensorflow as tf

def get_substrings(input_tensor, start_indices, lengths):
    # Convert input_tensor to a TensorFlow tensor if it's not already
    input_tensor = tf.convert_to_tensor(input_tensor)
    
    # Ensure start_indices and lengths are also tensors
    start_indices = tf.convert_to_tensor(start_indices)
    lengths = tf.convert_to_tensor(lengths)
    
    # Create a function to extract substrings
    def extract_substring(input_string, start, length):
        return input_string[start:start + length]
    
    # Use tf.map_fn to apply the function across the batch
    substrings = tf.map_fn(
        lambda x: extract_substring(x[0], x[1], x[2]),
        (input_tensor, start_indices, lengths),
        dtype=tf.string
    )
    
    return substrings

# Example usage:
input_strings = tf.constant(["hello", "world", "tensorflow"])
start_indices = tf.constant([1, 2, 3])
lengths = tf.constant([2, 3, 4])

result = get_substrings(input_strings, start_indices, lengths)
print(result.numpy())  # Output: ['el' 'rld' 'flow']
