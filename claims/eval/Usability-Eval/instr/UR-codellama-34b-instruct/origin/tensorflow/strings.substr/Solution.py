import tensorflow as tf

# Define a function to extract substrings from a tensor of strings
def extract_substrings(tensor, start, length):
  # Use tf.strings.substr to extract the substring from each element in the tensor
  extracted_strings = tf.strings.substr(tensor, start, length)
  
  # Return the extracted substrings as a new tensor
  return extracted_strings

# Test the function with some sample data
sample_data = tf.constant(['hello world', 'goodbye world', 'hello again'])
print(extract_substrings(sample_data, 0, 5)) # Should print ['hello', 'goodby']
