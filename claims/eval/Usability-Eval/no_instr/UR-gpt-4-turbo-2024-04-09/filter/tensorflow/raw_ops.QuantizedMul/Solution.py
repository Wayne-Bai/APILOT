import tensorflow as tf

# Define input data with quantized data types
x = tf.constant([1, 2, 3, 4], dtype=tf.int32)
y = tf.constant([10, 20, 30, 40], dtype=tf.int32)

# Normally, TensorFlow uses floating-point types for multiplication, so to simulate quantization:
# We will first define quantization parameters
x_min, x_max = 0, 5          # Min and max for x values
y_min, y_max = 0, 50         # Min and max for y values
x_scale = (x_max - x_min) / 255.0
y_scale = (y_max - y_min) / 255.0

# Convert integers to simulated quantized values
x_quant = tf.cast(x, tf.float32) * x_scale
y_quant = tf.cast(y, tf.float32) * y_scale

# Multiply quantized values
result_quant = tf.multiply(x_quant, y_quant)

# Convert the result back to integer representation (inverse quantization)
result_int = tf.cast(result_quant / (x_scale * y_scale), tf.int32)

print(result_int)
