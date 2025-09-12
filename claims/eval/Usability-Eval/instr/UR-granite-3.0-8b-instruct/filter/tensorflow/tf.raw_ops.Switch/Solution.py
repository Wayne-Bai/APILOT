import tensorflow as tf

# Assuming you have a tensor 'data' and a tensor 'pred'
# 'pred' is a tensor of type tf.int32 and shape [batch_size]

# Create a tensor of the same type and shape as 'pred'
# and fill it with zeros
zeros = tf.zeros_like(pred, dtype=tf.int32)

# Use tf.raw_ops.Switch to conditionally assign values to 'zeros'
# based on the values in 'pred'
switched = tf.raw_ops.Switch(data, pred, zeros)
