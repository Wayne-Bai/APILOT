import tensorflow as tf

@tf.RegisterGradient("QuantizeAndDequantizeV4Grad")
def _quantize_and_dequantize_v4_grad(op, grad):
    """Computes the gradients for `quantize_and_dequantize_v4`.

    Args:
        op: `QuantizeAndDequantizeV4` `Operation` that produced the `grad`.
        grad: Tensor, gradient with respect to output of the op.

    Returns:
        Gradients with respect to input of the op and None for the other argument.

    Raises:
        TypeError: if the operation was not an instance of `QuantizeAndDequantizeV4`.
    """
    op_type_attr = {"T", tf.dtypes.float32}
    inputs = list(op.inputs)
    inputs[0] = tf.compat.v1.assert_type(inputs[0], op_type_attr)
    return op.gradient(grad, inputs)

# Gradient test functionality

# Providing input tensors
x_input = tf.constant([0.1, 0.2, 0.3, 0.4, 0.5])
min_range = tf.constant(0)
max_range = tf.constant(1)
num_bits = tf.constant(8)

# Creating graph
qandd_op = tf.RawOps.QuantizeAndDequantizeV4(
    x=x_input,
    min_range=min_range,
    max_range=max_range,
    Tinput=tf.dtypes.float32,
    Toutput=tf.uint8,
    name="QAD"
)

# Compute gradients
grad = tf.gradients(qandd_op, [x_input])

# Run session
with tf.compat.v1.Session() as sess:
    grad_val = sess.run(grad)
    for val in grad_val:
        print(val)
