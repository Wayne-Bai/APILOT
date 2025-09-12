
import tensorflow as tf

# Create a placeholder tensor
a = tf.placeholder(tf.float32, shape=[2, 3])

# Define the transposed tensor
a_transposed = tf.transpose(a)

# Initialize the variables
init = tf.global_variables_initializer()

# Start a TensorFlow session
with tf.Session() as sess:
    sess.run(init)
    
    # Generate some sample data
    input_data = [[1, 2, 3], [4, 5, 6]]
    
    # Run the transposition operation
    result = sess.run(a_transposed, feed_dict={a: input_data})
    
    # Print the transposed tensor
    print(result)
