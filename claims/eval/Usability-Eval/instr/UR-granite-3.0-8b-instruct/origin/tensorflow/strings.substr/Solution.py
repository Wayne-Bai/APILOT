import tensorflow as tf

def get_substrings(input_tensor, start, end):
    # Ensure start and end are within the tensor's shape
    assert start >= 0 and end >= 0 and start < end
    assert end <= tf.shape(input_tensor)[1]

    # Get the substrings
    substrings = tf.string_split([input_tensor[:, start:end]], sep='')
    substrings = tf.squeeze(substrings, axis=1)

    return substrings

# Example usage:
input_tensor = tf.constant(["hello", "world", "tensorflow"])
start = 1
end = 4

result = get_substrings(input_tensor, start, end)
print(result)
