
import tensorflow as tf

# Define a tensor to be quantized and dequantized
input_tensor = tf.random.normal(shape=[10, 2], mean=0, stddev=1)

# Quantize the input tensor using the QuantizeAndDequantizeV4 function
quantized_tensor = tf.raw_ops.QuantizeAndDequantizeV4(input_tensor,
                                                       num_bits=8,
                                                       signed_input=True)

# Compute the gradient of the QuantizeAndDequantizeV4 operation using the gradient function
grad = tf.raw_ops.QuantizeAndDequantizeV4Grad(quantized_tensor,
                                              input_tensor,
                                              num_bits=8,
                                              signed_input=True)
