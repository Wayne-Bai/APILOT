import tensorflow as tf

def get_substrings(input_tensor, start_indices, lengths):
    # Convert input_tensor to a string tensor if it's not already
    input_tensor = tf.convert_to_tensor(input_tensor, dtype=tf.string)
    
    # Convert start_indices and lengths to tensors if they're not already
    start_indices = tf.convert_to_tensor(start_indices, dtype=tf.int32)
    lengths = tf.convert_to_tensor(lengths, dtype=tf.int32)
    
    # Create a function to get the substring for each element
    def substring_fn(x):
        string, start, length = x
        return tf.strings.substr(string, start, length)
    
    # Use tf.map_fn to apply the substring_fn to each element in the input_tensor
    substrings = tf.map_fn(substring_fn, (input_tensor, start_indices, lengths), dtype=tf.string)
    
    return substrings

# Example usage:
input_strings = ["hello", "world", "tensorflow"]
start_indices = [1, 2, 3]
lengths = [3, 2, 4]

result = get_substrings(input_strings, start_indices, lengths)
print(result.numpy())  # Output: ['ell' 'rl' 'flow']
