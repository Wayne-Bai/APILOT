
import tensorflow as tf

# Define inputs
x = tf.constant([1, 2, 3], dtype=tf.int8)
y = tf.constant([4, 5, 6], dtype=tf.int8)

# Quantize inputs
x_quant = tf.quantization.quantize(x, 0, -128, 127, tf.quint8)
y_quant = tf.quantization.quantize(y, 0, -128, 127, tf.quint8)

# Perform element-wise multiplication
result_quant = tf.raw_ops.QuantizedMul(x=x_quant, y=y_quant, Toutput=tf.quint8)

# Dequantize the result
result = tf.quantization.dequantize(result_quant, -128, 127) 

# Start session and run the operation
with tf.Session() as sess:
    output = sess.run(result)
    print(output)
