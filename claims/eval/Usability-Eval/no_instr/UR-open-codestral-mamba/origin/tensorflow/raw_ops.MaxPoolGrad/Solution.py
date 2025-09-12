import tensorflow as tf

# Create a random input tensor
input_tensor = tf.constant(np.random.rand(1, 5, 5, 1).astype(np.float32))

# Create a max pooling layer
max_pool = tf.nn.max_pool(input_tensor, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# Function to compute gradients of a max pooling operation
def compute_max_pooling_gradient(ops, grads):
  grad_ys = ops.Gradient("MaxPool", ops.output, grads)
  return [g.op.values[0] for g in grad_ys]

# Get the gradients of the max pooling operation
grads = compute_max_pooling_gradient(max_pool, tf.ones_like(max_pool))
