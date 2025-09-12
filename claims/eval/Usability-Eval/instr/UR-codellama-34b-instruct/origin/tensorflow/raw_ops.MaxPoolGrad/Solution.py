
import tensorflow as tf

# Define the input tensor and the pooling parameters
input_tensor = tf.placeholder(tf.float32, shape=(None, 100, 100))
window_size = 2
stride = 2
padding = 'SAME'

# Compute the maxpooling function using tf.nn.max_pool
pooled_output = tf.nn.max_pool(input_tensor, window_size, stride, padding)

# Compute the gradients of the maxpooling function using tf.gradients
grads = tf.gradients(pooled_output, input_tensor)

print(grads)
