
import tensorflow as tf

@tf.RegisterGradient("QuantizeAndDequantizeV4")
def _quantize_and_dequantize_v4_grad(op, grad):
    quantized = op.outputs[0]
    dequantized = op.inputs[0]
    
    # Compute gradient
    grad_quantized = grad
    grad_dequantized = grad * tf.cast(quantized, tf.float32)
    
    return grad_dequantized, None

# Example usage:
quantized_data = tf.Variable([0.3, 0.8, -1.2])
dequantized_data = tf.quantize_and_dequantize_v4(quantized_data)
loss = tf.reduce_sum(tf.square(dequantized_data))
gradients = tf.gradients(loss, quantized_data)
