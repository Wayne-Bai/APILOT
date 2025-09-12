# Import the necessary libraries
import tensorflow as tf

# Create a variable
var = tf.Variable([0.0, 0.0])

# Update the variable using sparse updates
indices = tf.constant([[0], [2]])
values = tf.constant([1.0, 3.0])
resource_sparseApplySparseSet = tf.raw_ops.ResourceScatterUpdate(ref=var, indices=indices, updates=values)

# Create a session and initialize the variable
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    # Apply the updates
    sess.run(resource_sparseApplySparseSet)
    
    # Print the updated variable
    print(sess.run(var))
