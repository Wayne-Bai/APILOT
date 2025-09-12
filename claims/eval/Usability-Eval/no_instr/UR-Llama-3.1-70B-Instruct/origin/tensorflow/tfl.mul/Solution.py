# Import necessary library
import tensorflow as tf

# Create two constant tensors
tensor_a = tf.constant([1, 2, 3, 4, 5])
tensor_b = tf.constant([5, 4, 3, 2, 1])

# Use the multiplication operator (*) for element-wise multiplication
result_mul = tensor_a * tensor_b

# Alternatively, use the tf.multiply function for element-wise multiplication
result_multiply = tf.multiply(tensor_a, tensor_b)

# Print the results
print("Result using multiplication operator (*):", result_mul)
print("Result using tf.multiply:", result_multiply)
