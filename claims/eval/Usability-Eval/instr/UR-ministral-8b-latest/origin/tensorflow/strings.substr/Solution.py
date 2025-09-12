import tensorflow as tf

# Function to extract substrings from a tensor of strings
def extract_substrings(tensor, start_index, end_index):
    tensor = tf.cast(tensor, dtype=tf.string)
    start_index = tf.expand_dims(start_index, axis=-1)
    end_index = tf.expand_dims(end_index, axis=-1)

    substrings = tf.strided_slice(tensor, start=start_index, end=start_index + end_index, name='strided_slice')

    return substrings

# Example usage
tensor_of_strings = tf.constant(["HelloWorld", "GoodbyeWorld", "GoodbyeAI"])
start_index = tf.constant([2])
end_index = tf.constant([5])

result = extract_substrings(tensor_of_strings, start_index, end_index)
print(result)
