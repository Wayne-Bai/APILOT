import tensorflow as tf

@tf.custom_gradient
def quantize_and_dequantize_v4_gradient(x):
    def grad(dy):
        # This is a simplistic gradient function for demonstration.
        # Typically, you'd compute a meaningful gradient here.
        return dy

    y = tf.quantization.quantize_and_dequantize_v2(x, input_min=tf.reduce_min(x), input_max=tf.reduce_max(x))
    return y, grad

# Example usage
x = tf.constant([1.5, 2.5, 3.5], dtype=tf.float32)
with tf.GradientTape() as tape:
    tape.watch(x)
    y = quantize_and_dequantize_v4_gradient(x)
dy_dx = tape.gradient(y, x)
print(dy_dx)
