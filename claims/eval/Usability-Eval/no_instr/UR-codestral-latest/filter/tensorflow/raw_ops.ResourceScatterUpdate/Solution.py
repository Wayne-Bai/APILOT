import tensorflow as tf
import numpy as np

# Create a TensorFlow variable with initial value
with tf.compat.v1.Session() as sess:
    value = tf.Variable(np.array([[1, 2], [3, 4]], dtype=np.float32), name='value')
    sess.run(tf.compat.v1.global_variables_initializer())

    # Define a sparse delta update. Indices and values are hardcoded for this example
    indices = [[0, 1], [1, 0]]  # positions to be updated in the tensor
    values = [100.0, 200.0]  # new values to put at the above positions

    # Convert indices and values to tensors
    indices = tf.constant(indices, dtype=tf.int64)
    values = tf.constant(values, dtype=tf.float32)

    # Apply the sparse update
    assign_op = tf.raw_ops.AssignVariableOp(
        resource=value.ref(),
        indices=[[0]]*len(indices),
        values=values,
        sparse_indices=indices,
        name="AssignVariableOp")
    sess.run(assign_op)

    # Print the updated tensor
    print(sess.run(value))
