# Importing required libraries
import tensorflow as tf

# Define a tensor
tensor = tf.constant([1, 2, 3, 4, 5, 6])

# Start a session
with tf.compat.v1.Session() as sess:
    # Add tensor to the current session's state
    tf.compat.v1.add_to_collection('my_tensor', tensor)

    # Run the op with the session. This will store the tensor's value in the session's state.
    sess.run(tensor)

    # Retrieve the tensor's value from the session's state
    tensor = tf.compat.v1.get_collection('my_tensor')[0]

# Now we can use the 'tensor' object outside the session to perform operations.
print(tensor.eval())
