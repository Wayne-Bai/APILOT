# Import the tensorflow library
import tensorflow as tf

# Create a tensor filled with a scalar value
tensor = tf.fill([3, 4], 5)

# Print the tensor
print(tensor)

# Define a session to evaluate the tensor
with tf.Session() as sess:
    # Evaluate the tensor
    result = sess.run(tensor)
    
    # Print the result
    print(result)
