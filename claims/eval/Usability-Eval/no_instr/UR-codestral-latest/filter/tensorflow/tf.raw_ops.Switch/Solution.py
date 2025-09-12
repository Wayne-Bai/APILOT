import tensorflow as tf

# Your tensors and predicate
data = tf.constant([1, 2, 3, 4, 5])
pred = tf.constant(True)  # This could be any condition that returns a boolean
output_true = tf.add(data, 5)  # Operations to perform if pred is True
output_false = tf.subtract(data, 5)  # Operations to perform if pred is False

# Use tf.raw_ops.Switch
output = tf.raw_ops.Switch(data=data, pred=pred, output_true=output_true, output_false=output_false)

# Create a session and run
with tf.Session() as sess:
    result = sess.run(output)
    print(result)
