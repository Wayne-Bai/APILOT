import tensorflow as tf

def _Switch(data, pred):
    # Create a switch node that forwards data to the output port determined by pred
    output_true, output_false = tf.raw_ops.Switch(data=data, pred=pred)
    return output_true, output_false

# Example usage
data = tf.constant([1.0, 2.0, 3.0])
pred = tf.constant(True)

output_true, output_false = _Switch(data, pred)

# Print the outputs
with tf.Session() as sess:
    print("Output True:", sess.run(output_true))
    print("Output False:", sess.run(output_false))
