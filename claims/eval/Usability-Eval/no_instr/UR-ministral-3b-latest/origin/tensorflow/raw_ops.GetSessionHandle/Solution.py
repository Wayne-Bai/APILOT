import tensorflow as tf

# Create some input data
input_data = tf.constant([1, 2, 3, 4], dtype=tf.float32)

# Store the input tensor in the session's state
handle = tf.raw_ops.tf_method(projector_name='tf_method', source_val=input_data, tensorstore=True)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run([handle]))  # Output will be the handle to the tensor
