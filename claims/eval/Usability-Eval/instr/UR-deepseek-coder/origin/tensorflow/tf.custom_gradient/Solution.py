import tensorflow as tf

@tf.custom_gradient
def custom_function(x):
    def grad(dy):
        return dy * (1 - x)
    return x * x, grad

# Example usage
x = tf.constant(2.0)
with tf.GradientTape() as tape:
    y = custom_function(x)

dy_dx = tape.gradient(y, x)
print(dy_dx.numpy())  # Output should be 0.0
