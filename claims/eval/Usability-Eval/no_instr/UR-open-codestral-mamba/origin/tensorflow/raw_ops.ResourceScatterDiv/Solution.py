import tensorflow as tf

# Create some initial tensors
x = tf.Variable([[0.1, 0.2], [0.3, 0.4]], dtype=tf.float32)
indices = tf.constant([[0, 0], [1, 1]], dtype=tf.int32)
updates = tf.constant([[0.1, 0.1], [0.1, 0.1]], dtype=tf.float32)
grads = tf.constant([[0.1, 0.0], [0.0, 0.1]], dtype=tf.float32)
a = tf.constant(0.001, dtype=tf.float32)

# Define the operation
with tf.control_dependencies(None):
    update = tf.raw_ops.SparseApplyAdagrad(
        x,
        indices,
        updates,
        grads,
        a,
        l1=0.001,
        l2=0.001
    )

# Run the operation
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(update)
    print(sess.run(x))
