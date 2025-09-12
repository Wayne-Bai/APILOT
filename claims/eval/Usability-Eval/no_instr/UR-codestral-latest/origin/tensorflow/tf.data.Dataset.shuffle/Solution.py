import tensorflow as tf
import numpy as np

# Assume we have some data
data = np.arange(10)

# Create a TensorFlow constant from the data
tensor_data = tf.constant(data)

# Create a shuffle operation
shuffled_data = tf.random.shuffle(tensor_data)

# Create a TensorFlow session
with tf.Session() as sess:
    # Initialize any variables (in this case, there are none)
    sess.run(tf.global_variables_initializer())

    # Run the shuffle operation
    result = sess.run(shuffled_data)

# Print the result
print(result)
