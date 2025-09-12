import tensorflow as tf

# Define a custom quantum operation
@tf.custom_gradient
def elementwise_quantized_multiply(x, y):
    def grad(delu):
        return delu * y
    def forward(x, y):
        return tf.raw_ops.Mul(x=x, y=y)
    return forward, grad

# Example usage:
x = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
y = tf.constant([4.0, 5.0, 6.0], dtype=tf.float32)

result = elementwise_quantized_multiply(x, y)
print(result.numpy())
