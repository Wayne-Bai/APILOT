import tensorflow as tf

def quantize_then_dequantize(tensor):
    # Quantize the tensor
    quantized_tensor = tf.quantization.fake_quant_with_min_max_args(tensor, min=-1.0, max=1.0, num_bits=8)

    # Dequantize the tensor
    dequantized_tensor = tf.fake_quant_with_min_max_args(quantized_tensor, min=-1.0, max=1.0, num_bits=8, narrow_range=True)

    return dequantized_tensor

# Test the function
with tf.Session() as sess:
    test_tensor = tf.constant([0.1, 0.2, 0.3, 0.4], dtype=tf.float32)
    result = sess.run(quantize_then_dequantize(test_tensor))
    print(result)
