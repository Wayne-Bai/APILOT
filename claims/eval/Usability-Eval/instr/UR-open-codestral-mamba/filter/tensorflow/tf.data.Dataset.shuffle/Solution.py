# Importing the tensorflow library
import tensorflow as tf

# Sample input data
data = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Shuffling the data randomly
shuffled_data = tf.random.shuffle(data)

# Session to run the shuffle operation
with tf.compat.v1.Session() as session:
    print(session.run(shuffled_data))
