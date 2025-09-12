import tensorflow as tf

# Assuming 'input' is your tensor
# Replace 'input' with your actual tensor
input_tensor = tf.quantization.fake_quant_with_min_max_args(
    input, min=-1, max=1, num_bits=8)

# Dequantize the input tensor into a bfloat16 Tensor
dequantized_tensor = tf.dtypes.cast(input_tensor, tf.bfloat16)
