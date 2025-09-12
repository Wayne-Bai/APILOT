import tensorflow as tf

# Define a variable and initialize it with some values
var = tf.Variable([[1.0, 2.0], [3.0, 4.0]])

# Define a sparse update tensor
indices = tf.constant([[0, 0], [1, 1]])
values = tf.constant([5.0, 6.0])

# Use tf.raw_ops.AssignSparse to update the variable
update = tf.raw_ops.AssignSparse(
    ref=var,
    indices=indices,
    values=values,
    use_locking=False
)

# Create a session and run the update operation
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(update)
    print(var.eval())
