import tensorflow as tf

# Create a simple tensor of float type.
x = tf.convert_to_tensor([0.0, 1.0, 2.0, 3.0, 4.0, 5.0], tf.float32)
x.shape

# Create a QuantizeAndDequantize op
q_op = tf.quantization.FakeQuantWithMinMaxVars(num_bits=8)
q_op_output = q_op(x)

# Calculate the gradients
with tf.GradientTape() as gt:
    gt.watch(x)
    y = q_op_output
grads = gt.gradient(y, x)
grads
