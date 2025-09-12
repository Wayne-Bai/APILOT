import tensorflow as tf

# Define the logits and the desired output shape
logits = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output_shape = (3, 3)

# Perform greedy decoding on the logits
decoded_indices = tf.greedy_decode(logits, output_shape)

# Print the decoded indices
print("Decoded Indices:")
print(decoded_indices)
