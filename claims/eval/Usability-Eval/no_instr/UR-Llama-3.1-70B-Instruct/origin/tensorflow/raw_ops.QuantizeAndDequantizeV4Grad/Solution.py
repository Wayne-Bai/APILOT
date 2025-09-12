import tensorflow as tf
import numpy as np

# Creating a simple constant tensor
input_tensor = tf.constant([1.0, 2.0, 3.0, -1.0, -2.0, -3.0], shape=[1, 2, 3])

# QuantizeAndDequantizeV4
quant_dequant_output = tf.raw_ops.QuantizeAndDequantizeV4(
    input=input_tensor,
    signed_input=False,
    num_bits=8,
    range_given=True,
    range_min=0,
    range_max=255,
    narrow_range=False
)

# Gradient of QuantizeAndDequantizeV4
with tf.GradientTape() as tape:
    tape.watch(input_tensor)
    gradient_output = tf.raw_ops.QuantizeAndDequantizeV4Grad(
        SX=input_tensor,
        Y=quant_dequant_output,
        signed_output=False
    )

# Print gradients
print(gradient_output)
