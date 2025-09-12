import tensorflow as tf

# Create a tensor, a condition and use tf.raw_ops to demonstrate switching based on the condition
tensor1 = tf.constant([10, 20])
tensor2 = tf.constant([15, 25])

# Condition tensor where True means tensor1 will be selected, and False means tensor2
pred = tf.constant(True)

# Using tf.raw_ops.Switch to forward data to the output port determined by pred
output_true, output_false = tf.raw_ops.Switch(data=tensor1, pred=pred)

# To see the effect, we will use output_true and output_false
# Depending on 'pred', output_true or output_false will carry the 'data', and another would be empty
with tf.Session() as sess:
    result_true, result_false = sess.run([output_true, output_false])
    print("Output True:", result_true)
    print("Output False:", result_false)
