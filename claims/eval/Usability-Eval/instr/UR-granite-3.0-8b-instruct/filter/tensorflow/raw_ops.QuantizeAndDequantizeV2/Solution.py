import tensorflow as tf

def quantize_and_dequantize(tensor):
    # Quantize the tensor
    quantized_tensor = tf.raw_ops.QuantizeV2(tensor, tf.int32.min, tf.int32.max, tf.int32.num)

    # Dequantize the tensor
    dequantized_tensor = tf.raw_ops.Dequantize(quantized_tensor, tf.int32.min, tf.int32.max, tf.float32.num)

    return dequantized_tensor
