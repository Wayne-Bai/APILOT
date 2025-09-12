import tensorflow as tf

# Tensor representing the data to be forwarded
data = tf.constant([10, 20, 30, 40, 50])

# Boolean tensor determining to which output the data should be sent
pred = tf.constant([True, False, True, True, False])

# Using tf.raw_ops.RefSwitch to forward data based on the predicate
outputs = tf.raw_ops.RefSwitch(data=data, pred=pred)

# Printing the outputs
print("True branch output:", outputs.output_true)
print("False branch output:", outputs.output_false)
