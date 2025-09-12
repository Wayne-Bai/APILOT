import tensorflow as tf

# Create a tensor of strings
input_tensor = tf.constant(["Hello", "World", "TensorFlow"])

# Define a function to extract substrings
def extract_substrings(input_tensor, start, end):
    return input_tensor[start:end]

# Use the function to extract substrings
start_indices = [0, 3, 6]
end_indices = [2, 5, 8]

output_tensors = [extract_substrings(input_tensor, start, end) for start, end in zip(start_indices, end_indices)]

# Print the output tensors
print(output_tensors)
