import tensorflow as tf

# Create a tensor of strings
input_tensor = tf.constant(["Hello", "World", "This", "is", "a", "test"])

# Specify the substring length
substr_length = 3

# Function to generate substrings
def generate_substrings(tensor, substr_length):
    # Create a shape for reshaping the tensor
    shape = tf.shape(tensor)

    # Calculate number of strides
    num_strides = shape[0] - substr_length + 1

    # Create a tensor of indices
    indices = tf.expand_dims(tf.range(num_strides), 0)

    # Generate sliding windows
    windows = tf.expand_dims(tensor, 0)[:, indices, :]
    windows = tf.squeeze(windows, 0)

    # Concatenate the windows along the last axis
    result = tf.concat([windows[i: i + substr_length] for i in range(windows.shape[0] - substr_length + 1)], axis=-1)
    return result

# Use the function to get substrings
output_tensor = generate_substrings(input_tensor, substr_length)
print(output_tensor)
