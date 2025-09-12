import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([1.0, 2.0, 3.0])

# Define a variable to store the tensor value
stored_tensor = tf.raw_ops.CheckpointUtils.save_value(input_tensor, [input_tensor])

# Create a session and initialize the variable
with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    stored_value = sess.run(stored_tensor)

    # Optionally, you can also restore the value
    restored_tensor = tf.raw_ops.CheckpointUtils.restore_value(stored_value)

    print("Stored Value:", stored_value)
    print("Restored Value:", sess.run(restored_tensor))
