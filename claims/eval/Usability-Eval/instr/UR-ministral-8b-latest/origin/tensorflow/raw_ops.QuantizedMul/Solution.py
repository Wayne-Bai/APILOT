import tensorflow as tf

def scaled_elementwise_multiply(x, y):
    @tf.function
    def multiply(x, y):
        return tf.raw_ops.Mul(x, y)

    return multiply(x, y)

# Example usage
x = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)
y = tf.constant([10.0, 20.0, 30.0, 40.0], dtype=tf.int32)
result = scaled_elementwise_multiply(x, y)

print(result)
