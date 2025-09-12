
import tensorflow as tf

# Define a tensor of strings
tensor_of_strings = tf.constant(["Hello", "World", "TensorFlow", "Substring"])

# Define start and end indices for substrings
start_idx = tf.constant([0, 1, 2, 3])
end_idx = tf.constant([2, 3, 5, 7])

# Extract substrings using strided_slice
substrings = tf.strided_slice(tensor_of_strings, start_idx, end_idx, [1])

# Run a TensorFlow session to evaluate the substrings
with tf.Session() as sess:
    result = sess.run(substrings)
    print(result)
