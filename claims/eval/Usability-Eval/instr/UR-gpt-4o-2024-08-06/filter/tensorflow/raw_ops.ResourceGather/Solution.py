import tensorflow as tf

# Create a variable to demonstrate the gather operation
variable = tf.Variable([[1, 2], [3, 4], [5, 6]])

# Define the indices to gather
indices = [0, 2]

# Use the tf.gather method to gather slices based on the indices
gathered_slices = tf.gather(variable, indices)

# Initialize the variables
init_op = tf.compat.v1.global_variables_initializer()

# Create a session and run the initialization
with tf.compat.v1.Session() as sess:
    sess.run(init_op)
    result = sess.run(gathered_slices)
    print("Gathered Slices:\n", result)
