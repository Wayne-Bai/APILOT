Python
import tensorflow as tf

# Create a resource variable
var = tf.Variable(tf.zeros([10]))

# Create an indices tensor and a values tensor
indices = tf.constant([[4], [3], [1]])
values = tf.constant([9, 10, 11], dtype=tf.float32)

# Create a shape tensor
shape = tf.constant([10], dtype=tf.int64)

# Use tf.raw_ops.SparseAssign to assign sparse updates to the variable
update_op = tf.raw_ops.SparseAssign(
    ref=var,
    indices=indices,
    values=values,
    dense_shape=shape
)

# Initialize the variables
init_op = tf.global_variables_initializer()

# Create a session and run the operations
with tf.Session() as sess:
    sess.run(init_op)
    sess.run(update_op)
    print(sess.run(var))
