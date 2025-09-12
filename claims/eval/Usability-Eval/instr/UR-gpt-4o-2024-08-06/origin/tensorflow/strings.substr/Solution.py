import tensorflow as tf

# Sample tensor of strings
strings = tf.constant(["hello world", "tensorflow is great", "substring example"])

# Define start and end indices for substrings extraction
start_indices = tf.constant([0, 10, 0])   # Start at beginning for all
end_indices = tf.constant([5, 18, 9])    # End indices for each string

# Function to extract substrings from tensor
def extract_substrings(strings, start_indices, end_indices):
    substrings = []
    for index, element in enumerate(strings.numpy()):
        start = start_indices[index]
        end = end_indices[index]
        substring = element[start:end]
        substrings.append(substring.decode('utf-8'))
    return substrings

# Extract subtrings
substrings = extract_substrings(strings, start_indices, end_indices)

# Print the result
print(substrings)
