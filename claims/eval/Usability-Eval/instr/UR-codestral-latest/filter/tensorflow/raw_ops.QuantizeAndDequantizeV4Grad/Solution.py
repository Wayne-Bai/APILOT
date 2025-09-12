import tensorflow as tf

def compute_gradients(inputs, min_range, max_range):
    with tf.GradientTape() as tape:
        tape.watch(inputs)
        quantized = tf.quantization.quantize(inputs, min_range, max_range, tf.float32, 'quantized')
        dequantized = tf.quantization.dequantize(quantized.output, min_range, max_range, 'dequantized')
    grad = tape.gradient(dequantized, inputs)
    return grad

# Example usage:
inputs = tf.constant([[1.2, 2.3, -3.4], [4.5, -6.7, 8.9]], dtype=tf.float32)
min_range = tf.constant(-10.0, dtype=tf.float32)
max_range = tf.constant(10.0, dtype=tf.float32)
gradients = compute_gradients(inputs, min_range, max_range)
