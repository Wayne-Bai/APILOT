# Importing the necessary libraries
import tensorflow as tf

# Defining two tensors for element-wise multiplication
tensor1 = tf.constant([1, 2, 3, 4])
tensor2 = tf.constant([5, 6, 7, 8])

# Using the multiplication operator (*) for element-wise multiplication
result = tensor1 * tensor2

# Alternative method using the multiply function from tensorflow
result_alt = tf.multiply(tensor1, tensor2)

# Printing the results
print("Result using * operator: ", result)
print("Result using multiply function: ", result_alt)
