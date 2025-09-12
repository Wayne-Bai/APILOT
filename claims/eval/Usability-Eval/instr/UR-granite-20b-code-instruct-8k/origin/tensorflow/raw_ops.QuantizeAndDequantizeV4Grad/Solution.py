
import tensorflow as tf
quantize_v4_grad_op = tf.raw_ops.QuantizeAndDequantizeV4Grad(input=input, input_min=input_min, input_max=input_max, num_bits=num_bits, signed_input=signed_input, range_given=range_given, round_mode=round_mode,narrow_range=narrow_range, axis=axis)
