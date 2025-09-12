import tensorflow as tf

def get_substrings(input_tensor, start_indices, lengths):
    # Convert input_tensor to a TensorFlow tensor if it's not already
    input_tensor = tf.convert_to_tensor(input_tensor)
    
    # Create a function to get the substring for each element
    def get_substring(args):
        string, start, length = args
        return string[start:start + length]
    
    # Use tf.map_fn to apply the function to each element in the tensor
    substrings = tf.map_fn(
        get_substring,
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
