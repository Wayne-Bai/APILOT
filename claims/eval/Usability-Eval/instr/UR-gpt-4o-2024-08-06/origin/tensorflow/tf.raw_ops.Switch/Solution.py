import tensorflow as tf

# Set up some sample input data
data_true = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
data_false = tf.constant([-1.0, -2.0, -3.0], dtype=tf.float32)
pred = tf.constant(True)

# Use tf.raw_ops.Switch to forward data based on the prediction
output_true, output_false = tf.raw_ops.Switch(data=data_true, pred=pred)

with tf.Session() as sess:
    # Run the graph and print outputs
    result_true = sess.run(output_true)
    print("Output when pred is True:", result_true)
    
    # Change prediction to False and test
    pred = tf.constant(False)
    output_true, output_false = tf.raw_ops.Switch(data=data_false, pred=pred)
    result_false = sess.run(output_false)
    print("Output when pred is False:", result_false)
