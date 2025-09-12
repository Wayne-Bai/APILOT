import tensorflow as tf

# Define the sparse update indices and values
indices = [10, 20, 30, 40, 50]
values = [0.1, 0.2, 0.3, 0.4, 0.5]

# Create a resource variable to store the sparse updates
var = tf.Variable(tf.zeros([64]), dtype=tf.float32)

# Define the scatter update operation
sparse_update = tf.raw_ops.ScatterUpdate(ref=var, indices=indices, updates=values)

# Run the scatter update operation
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print("Before sparse update: ", var.eval())
    sess.run(sparse_update)
    print("After sparse update: ", var.eval())
