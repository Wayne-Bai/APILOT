
import tensorflow as tf

# Create a tensor with some sample data
data = [1, 2, 3, 4]
tensor = tf.constant(data)

# Capture the tensor in the current session
handle = tf.capture_tensor(tensor)

# Use the handle to retrieve the tensor's value
value = handle.eval()

print(value)
