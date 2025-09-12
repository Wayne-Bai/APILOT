import tensorflow as tf

def compute_gradients(x, filter):
  with tf.GradientTape() as tape:
    tape.watch(x)
    conv = tf.nn.conv2d(x, filter, strides=[1, 1, 1, 1], padding='SAME')
  grads = tape.gradient(conv, x)
  return grads

# Initialize input and filter
x = tf.random.normal([1, 10, 10, 1])
filter = tf.random.normal([3, 3, 1, 1])

# Compute gradients
gradients = compute_gradients(x, filter)
