import tensorflow as tf

# Define a sparse tensor to update
indices = tf.constant([[0, 0], [1, 2]], dtype=tf.int64)
values = tf.constant([1.0, 2.0], dtype=tf.float32)
sparse_tensor = tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=[3, 4])

# Create a variable to update
variable = tf.Variable(tf.zeros([3, 4], dtype=tf.float32))

# Perform sparse updates
update = tf.tensor_scatter_nd_update(variable, indices, values)

# To execute the update in a TensorFlow session (Eager execution is default in TF 2.x)
tf.print("Before update:", variable)
variable.assign(update)
tf.print("After update:", variable)
