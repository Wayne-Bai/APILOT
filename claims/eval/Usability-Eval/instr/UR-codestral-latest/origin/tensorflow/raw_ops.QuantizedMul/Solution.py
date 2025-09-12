import tensorflow as tf

# Suppose x and y are your quantized tensors
x = tf.quantization.quantize(tf.constant([1.0, 2.0]), tf.float32, axis=-1)
y = tf.quantization.quantize(tf.constant([3.0, 4.0]), tf.float32, axis=-1)

# Element-wise multiplication
result = tf.raw_ops.Mul(x=x, y=y)

# To see the result, we need to dequantize it
dequantized_result = tf.quantization.dequantize(result, tf.float32)

with tf.Session() as sess:
    print(sess.run(dequantized_result))
