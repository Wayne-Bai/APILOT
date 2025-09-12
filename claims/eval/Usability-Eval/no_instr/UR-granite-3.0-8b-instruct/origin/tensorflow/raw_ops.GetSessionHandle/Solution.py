import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Get the value of the tensor in the current session
tensor_value = tensor.numpy()

print(tensor_value)
