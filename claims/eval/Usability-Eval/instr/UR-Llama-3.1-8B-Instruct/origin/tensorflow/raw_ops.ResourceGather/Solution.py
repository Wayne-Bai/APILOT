import tensorflow as tf

# Create a variable
resource = tf.Variable([1, 2, 3, 4, 5])

# Define the indices to gather slices
indices = tf.constant([1, 3])

# Use tf.gather to gather slices from the variable
result = tf.gather(resource, indices)

with tf.Session() as sess:
    # Initialize the variable
    sess.run(tf.global_variables_initializer())
    
    # Run the operation
    result_value = sess.run(result)
    print(result_value)
