import tensorflow as tf

@tf.function
def quantize_and_dequantize_gradient(grad, inputs):
    output = tf.raw_ops.QuantizeAndDequantizeV4Grad(grad=grad, inputs=inputs)
    return output
