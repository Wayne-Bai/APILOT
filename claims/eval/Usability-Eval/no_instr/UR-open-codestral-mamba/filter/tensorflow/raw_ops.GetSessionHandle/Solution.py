import tensorflow as tf
tf.compat.v1.disable_v2_behavior()

# Define a tensor.
X = tf.compat.v1.Variable(tf.compat.v1.ones([1]))

# Store the input tensor in the state of the current session.
with tf.compat.v1.Session() as sess:
    sess.run(X.initializer)

    # Capture the tensor's current value
    value = sess.run(X)

    # Store the value
    handle = X.handle
    cold = tf.compat.v1.contrib.saved_model.ReadOperation(
        dtypes=[tf.float32],
        tensor_names=["tensor_name"],
        shape=[tf.contrib.saved_model.TensorInfo.TensorShape()],
        handle=handle
    )

    print(sess.run(cold), value)  # => [1.] [1.]
