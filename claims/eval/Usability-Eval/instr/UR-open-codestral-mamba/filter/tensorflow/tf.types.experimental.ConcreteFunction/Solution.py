import tensorflow as tf

# Create a custom-gradient function
@tf.custom_gradient
def custom_func(x):
  """Computes square of input 'x'."""

  # Forward computation
  y = tf.square(x)

  # Gradient computation
  def grad(dy):
    return 2 * x * dy

  # Return the output of the forward computation, and the gradient function
  return y, grad

# Test the custom function
x = tf.constant(3.)
with tf.GradientTape() as t:
  t.watch(x)
  y = custom_func(x)
dy_dx = t.gradient(y, x)

print(y.numpy(), dy_dx.numpy())
