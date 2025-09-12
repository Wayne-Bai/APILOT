import tensorflow as tf

# Define a sample tensor
tensor = tf.constant([[10, 20, 30], [40, 50, 60], [70, 80, 90]], dtype=tf.float32)

# Specify the number of largest values to find
k = 2

# Find the k largest values and their indices along the last dimension
values, indices = tf.nn.top_k(tensor, k)

# Print the results
print("k largest values:\n", values.numpy())
print("Indices of k largest values:\n", indices.numpy())
