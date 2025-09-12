import tensorflow as tf

def forward_data(pred, inputs):
    return tf.raw_ops.Switch(data=inputs, pred=pred, name=None)

# example usage:
inputs = tf.constant([1, 2, 3, 4, 5])
pred = tf.constant(True)
output_true, output_false = forward_data(pred, inputs)
