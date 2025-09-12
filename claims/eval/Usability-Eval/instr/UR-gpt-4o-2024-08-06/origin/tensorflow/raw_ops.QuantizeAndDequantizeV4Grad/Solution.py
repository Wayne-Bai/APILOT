import tensorflow as tf

def quantize_and_dequantize_v4_grad(inputs, input_min, input_max, 
                                    backprop_wrt_input=True, backprop_wrt_minmax=True):
    # Create a quantizer to mimic the quantization profile
    quantizer = tf.quantization.fake_quant_with_min_max_vars(
        inputs, input_min, input_max, num_bits=8, narrow_range=False)

    # Calculate the gradients
    with tf.GradientTape(persistent=True) as tape:
        tape.watch([inputs, input_min, input_max])
        quantized = tf.quantization.fake_quant_with_min_max_vars(
            inputs, input_min, input_max, num_bits=8, narrow_range=False)

    # Derivatives with respect to the inputs
    grads = tape.gradient(quantized, [inputs, input_min, input_max])
    gradients = []
    
    if backprop_wrt_input:
        gradients.append(grads[0])  # Gradient with respect to inputs
    if backprop_wrt_minmax:
        gradients.extend(grads[1:])  # Gradient with respect to min and max
    
    del tape
    return tuple(gradients) if len(gradients) > 1 else gradients[0]

# Usage example
input_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=tf.float32)
input_min = tf.constant(1.0, dtype=tf.float32)
input_max = tf.constant(6.0, dtype=tf.float32)

grads = quantize_and_dequantize_v4_grad(input_tensor, input_min, input_max)
print('Gradients:', grads)
