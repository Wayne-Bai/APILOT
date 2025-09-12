import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Get the session
session = tf.compat.v1.Session()

# Get the lower-level TensorFlow operation to capture a tensor's value
capture_tensor_value_op = tf.raw_ops.CaptureTensorValue(tensor)

# Execute the operation
result = capture_tensor_value_op.eval(session)

# Print the result
print(result)
