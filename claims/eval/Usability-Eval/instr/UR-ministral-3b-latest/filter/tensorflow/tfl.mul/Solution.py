import tensorflow as tf

# Definition of a function which performs element-wise multiplication
def element_wise_multiply(x, y):
    result = x * y
    return result

# Example usage:
x = tf.constant([[1, 2, 3], [4, 5, 6]])
y = tf.constant([[7, 8, 9], [10, 11, 12]])

result = element_wise_multiply(x, y)

print(result.numpy())  # Print the result as a numpy array
