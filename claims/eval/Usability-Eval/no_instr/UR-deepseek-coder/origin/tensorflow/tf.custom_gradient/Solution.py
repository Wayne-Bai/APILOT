import tensorflow as tf

@tf.custom_gradient
def custom_function(x):
    def grad(dy):
        return dy * 2 * x  # Custom gradient calculation
    return x * x, grad

# Example usage
x = tf.constant(3.0)
with tf.GradientTape() as tape:
    tape.watch(x)
    y = custom_function(x)

gradient = tape.gradient(y, x)
print(gradient.numpy())  # Output should be 6.0
