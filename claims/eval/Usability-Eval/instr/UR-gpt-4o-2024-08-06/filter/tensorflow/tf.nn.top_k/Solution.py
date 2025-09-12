import tensorflow as tf

# Function to find the k largest values and their indices along the last dimension
def find_k_largest(tensor, k):
    # Find the largest values and their indices along the last dimension
    values, indices = tf.math.top_k(tensor, k=k, sorted=True)
    
    return values, indices

# Sample data tensor
data = tf.constant([[1, 3, 5, 7],
                    [4, 6, 8, 2],
                    [9, 0, 3, 1]], dtype=tf.float32)

# Specify the number of largest values/indices to find
k = 2

# Call the function
largest_values, largest_indices = find_k_largest(data, k)

# Evaluate the tensors (This step should be run within a session if using TensorFlow 1.x)
# In TensorFlow 2.x, eager execution is enabled by default, so we can directly print
print("Largest values:", largest_values.numpy())
print("Indices of the largest values:", largest_indices.numpy())
