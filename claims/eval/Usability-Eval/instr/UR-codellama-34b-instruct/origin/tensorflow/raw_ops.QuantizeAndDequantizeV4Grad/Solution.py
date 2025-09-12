
import tensorflow as tf
from tensorflow.python.ops import array_ops

def quantize_and_dequantize_v4(inputs, input_min, input_max, axis=None):
    # Calculate gradients for QuantizeAndDequantizeV4 op
    
    # Calculate the scale and zero point from the input range
    scale = (input_max - input_min) / 255.0
    zero_point = tf.cast(input_min, dtype=tf.int32)
    
    # Quantize the inputs using the calculated scale and zero point
    quantized_inputs = tf.round(scale * (inputs - zero_point)) + zero_point
    
    # Calculate the gradient for each input element
    gradients = array_ops.zeros_like(quantized_inputs, dtype=tf.float32)
    for i in range(len(quantized_inputs)):
        if quantized_inputs[i] > 0:
            # Calculate the gradient for positive inputs
            gradients[i] = 1 / scale
        elif quantized_inputs[i] < 0:
            # Calculate the gradient for negative inputs
            gradients[i] = -1 / scale
        else:
            # Calculate the gradient for zero inputs
            gradients[i] = 0.0
    
    return gradients
