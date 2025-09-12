import tensorflow as tf

def quantize_and_dequantize(tensor):
    # Quantize the tensor
    quantized_tensor = tf.raw_ops.QuantizeV2(
        input=tensor,
        min=tf.reduce_min(tensor),
        max=tf.reduce_max(tensor),
        num_bits=8,
        narrow_range=False
    )

    # Dequantize the tensor
    dequantized_tensor = tf.raw_ops.Dequantize(
        input=quantized_tensor,
        min=tf.reduce_min(tensor),
        max=tf.reduce_max(tensor),
        num_bits=8,
        narrow_range=False
    )

    return dequantized_tensor
