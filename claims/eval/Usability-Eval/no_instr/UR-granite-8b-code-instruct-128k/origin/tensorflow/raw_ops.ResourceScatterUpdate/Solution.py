import tensorflow as tf

# Define the variable to be updated
var = tf.Variable([[1, 2], [3, 4]])

# Define the sparse indices and updates
indices = tf.constant([[0, 1], [1, 0]])
updates = tf.constant([[10, 20], [30, 40]])

# Use the ResourceScatterUpdate function to perform the sparse update
with tf.GradientTape() as tape:
    tape.watch(var)
    new_var = tf.raw_ops.ResourceScatterUpdate(
        resource=var,
        indices=indices,
        updates=updates
    )

# Print the updated variable
print(new_var)
