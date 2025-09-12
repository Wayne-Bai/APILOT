import tensorflow as tf

# Create a function to calculate the gradient of QuantizeAndDequantizeV4
def grad_quantize_quantize_v4(input_tensor, second_tensor, qparams, dequantize_algorithm):
    # Define operations using raw ops
    quantize_operation = tf.raw_ops.QuantizeAndDequantizeV4(
        x=input_tensor,
        weight=qparams,
        dequantize_algorithm=dequantize_algorithm
    )
    grads = tf.GradientTape(watches=[input_tensor]).gradient(second_tensor, input_tensor)

    return grads
