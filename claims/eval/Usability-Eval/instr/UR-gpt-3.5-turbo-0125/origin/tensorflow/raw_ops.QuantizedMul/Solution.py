
import tensorflow as tf

# Define the two input quantized tensors
x = tf.quantization.quantize(20.0, 1.0, -128, 127, tf.quint8, mode='MIN_FIRST')
y = tf.quantization.quantize(30.0, 1.0, -128, 127, tf.quint8, mode='MIN_FIRST')

# Perform element-wise multiplication on the quantized tensors
result = tf.raw_ops.QuantizedMul(x=x, y=y, Toutput=tf.quint8)

# Dequantize the result if necessary
result_dequant = tf.quantization.dequantize(input=result.output, min_range=result.output_min, max_range=result.output_max, T=tf.float32)

# Start a TensorFlow session to execute the operations
with tf.Session() as sess:
    output = sess.run(result)
    dequant_output = sess.run(result_dequant)
    print("Quantized result:", output)
    print("Dequantized result:", dequant_output)
