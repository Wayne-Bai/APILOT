import tensorflow as tf

@tf.raw_ops.video_ops.Multiply
def multiply_quantized(x, y):
    return x * y

# Example usage:
x = tf.convert_to_tensor([1, 2, 3], dtype=tf.int8)
y = tf.convert_to_tensor([4, 5, 6], dtype=tf.int8)
result = multiply_quantized(x, y)

print(result)
