# Importing necessary libraries
import tensorflow as tf
import numpy as np

# Defining the function
def custom_quantize_and_dequantize_v4_grad(gradients, inputs, 
                                           min_range=tf.constant(-128.0),
                                           max_range=tf.constant(127.0),
                                           num_bits=8,
                                           narrow_range=False,
                                           signed_input=True):

    # Calculate the scale factor
    scale_factor = (max_range - min_range) / (2 ** num_bits - 1)

    # Clip the inputs to min and max range
    clipped_inputs = tf.clip_by_value(inputs, min_range, max_range)

    # Quantize the inputs
    quantized_inputs = tf.cast(tf.round(clipped_inputs / scale_factor), tf.int32)

    # Dequantize the inputs
    dequantized_inputs = tf.cast(quantized_inputs, tf.float32) * scale_factor

    # Calculate the gradient of the dequantized input with respect to the input
    grad_dequantized_wrt_input = tf.ones_like(inputs)

    # Calculate the gradient of the quantized input with respect to the input
    grad_quantized_wrt_input = tf.where(tf.equal(tf.sign(dequantized_inputs), tf.sign(clipped_inputs)), 
                                        tf.ones_like(inputs), 
                                        tf.zeros_like(inputs))

    # Calculate the final gradient
    final_grad = grad_dequantized_wrt_input * grad_quantized_wrt_input * gradients

    return final_grad

# Example usage
with tf.GradientTape() as tape:
    inputs = tf.Variable(tf.random.normal([5]))
    min_range = tf.constant(-128.0)
    max_range = tf.constant(127.0)
    num_bits = 8
    narrow_range = False
    signed_input = True

    outputs = tf.where(tf.greater(inputs, max_range), 
                       max_range * tf.ones_like(inputs), 
                       tf.where(tf.less(inputs, min_range), 
                                min_range * tf.ones_like(inputs), 
                                custom_quantize_and_dequantize_v4_grad(
                                               tf.ones_like(inputs), inputs, min_range, max_range, num_bits, narrow_range, signed_input)))

gradients = tape.gradient(outputs, inputs)
