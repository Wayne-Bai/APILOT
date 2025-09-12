import tensorflow as tf

def add_bias_quantized(input_tensor, bias_tensor, input_dtype=tf.int8, bias_dtype=tf.int32):
    # Ensure the input is quantized
    input_tensor = tf.cast(input_tensor, input_dtype)
    bias_tensor = tf.cast(bias_tensor, bias_dtype)

    # Adding bias to the quantized input
    output_tensor = tf.quantization.quantized_add(input_tensor, bias_tensor, input_dtype=input_dtype, bias_dtype=bias_dtype)

    return output_tensor
