import tensorflow as tf

# Assume var is a handle to a variable to be updated
# Assume indices and updates are tensors containing sparse updates
def sparse_update(var, indices, updates):
    with tf.Session() as sess:
      # Create and initialize variable
      var = tf.Variable(tf.zeros([10,]))
      init = tf.global_variables_initializer()
      sess.run(init)

      # Prepare sparse update operation
      update = tf.raw_ops.SparseApplyAdd(resource=var.handle, indices=indices, updates=updates)

      # Run update operation
      sess.run(update)

      # View the updated variable
      print(sess.run(var))

# Testing the function
indices = tf.constant([2, 5])
updates = tf.constant([9, 10])
sparse_update(var, indices, updates)
