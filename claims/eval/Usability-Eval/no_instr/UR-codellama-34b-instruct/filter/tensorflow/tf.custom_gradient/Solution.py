import tensorflow as tf

# Define the function with the custom gradient
@tf.custom_gradient
def my_function(x):
    y = tf.sin(x)
    grad = lambda g: tf.cos(g)
    return y, grad

# Test the function
x = tf.constant(0.)
y = my_function(x)
print(y)  # prints tf.Tensor(1., shape=(), dtype=float32)
