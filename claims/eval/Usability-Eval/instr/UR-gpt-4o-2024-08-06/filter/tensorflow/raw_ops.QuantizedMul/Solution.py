import tensorflow as tf

# Defining quantized multiplication using TensorFlow
def quantized_multiply(x, y, min_x, max_x, min_y, max_y):
    # Quantize the input tensors
    quant_x = tf.quantization.quantize(x, min_x, max_x, tf.qint32)
    quant_y = tf.quantization.quantize(y, min_y, max_y, tf.qint32)

    # Get the quantized values
    quantized_x = quant_x.output
    quantized_y = quant_y.output

    # Perform element-wise multiplication on quantized values
    quant_product = tf.raw_ops.QuantizedMul(
        x=quantized_x,
        y=quantized_y,
        min_x=quant_x.output_min,
        max_x=quant_x.output_max,
        min_y=quant_y.output_min,
        max_y=quant_y.output_max,
        Toutput=tf.qint32
    )

    # Dequantize the result
    dequantized_result = tf.quantization.dequantize(
        quant_product.z,
        min_range=quant_product.min_z,
        max_range=quant_product.max_z
    )

    return dequantized_result

# Example inputs
x = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
y = tf.constant([4.0, 5.0, 6.0], dtype=tf.float32)

# Define the ranges for quantization
min_x = 1.0
max_x = 3.0
min_y = 4.0
max_y = 6.0

# Perform quantized multiplication
result = quantized_multiply(x, y, min_x, max_x, min_y, max_y)
print("Result of quantized multiplication:", result.numpy())
