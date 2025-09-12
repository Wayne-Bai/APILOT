import tensorflow as tf

# Define your Python function
def add_tensors(tensor1, tensor2):
    return tensor1 + tensor2

# Define a TensorFlow operation using the Python function
add_tensor = tf.python_function(add_tensors, [tf.TensorSpec(None, tf.float32), tf.TensorSpec(None, tf.float32)], tf.float32)

# Create TensorFlow tensors
tensor1 = tf.constant([1.0, 2.0, 3.0])
tensor2 = tf.constant([4.0, 5.0, 6.0])

# Use the TensorFlow operation
result = add_tensor(tensor1, tensor2)

# Print the result
print(result.numpy())
