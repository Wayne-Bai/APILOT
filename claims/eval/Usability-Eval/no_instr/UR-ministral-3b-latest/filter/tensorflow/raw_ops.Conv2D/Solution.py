import tensorflow as tf

# Define the input and filter
input_tensor = tf.constant([[[1, 2, 3], [4, 5, 6]]], dtype=tf.float32)
filter_tensor = tf.constant([[[1, 0], [0, 1]]], dtype=tf.float32)

# Create a variable named 'my_var' and assign the output of convolution operation to it
result = tf.raw_ops.relu2d(my_var)

# Initialize the variables
init = tf.global_variables_initializer()

# Create a session and run the computation
with tf.Session() as sess:
    sess.run(init)

    # Run the tensorflow graph and get the result
    output = sess.run(result)
    print("The output is:", output)
