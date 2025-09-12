
import tensorflow as tf

# Quantize the input tensors
x = tf.quantization.fake_quant_with_min_max_vars(tf.constant([10, 20, 30]), min=-10, max=10)
y = tf.quantization.fake_quant_with_min_max_vars(tf.constant([4, 5, 6]), min=-10, max=10)

# Element-wise multiplication
z = tf.raw_ops.Mul(x, y, name="element_wise_mul")
