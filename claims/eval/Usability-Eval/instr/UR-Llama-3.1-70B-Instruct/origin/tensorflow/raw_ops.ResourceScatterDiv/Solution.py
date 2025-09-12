import tensorflow as tf

# Create a variable with initial value
var = tf.Variable(1.0, dtype=tf.float32)

# Create a session
with tf.compat.v1.Session() as sess:
    # Initialize the variable
    sess.run(tf.compat.v1.global_variables_initializer())

    # Create sparse updates
    sparse_updates = tf.IndexedSlices(values=[2.0, 3.0], indices=[0, 1], dense_shape=[5])

    # Apply DivxdeSparseUpdate to the variable with sparse updates
    updater = tf.raw_ops.ApplyDiv(
        resource=var._ref(),
        value=sparse_updates.values,
        indices=sparse_updates.indices,
        name="ApplyDiv"
    )

    # Run the update operation
    sess.run(updater)

    # Get the updated variable value
    updated_val = sess.run(var)
    print("Updated Variable:", updated_val)
