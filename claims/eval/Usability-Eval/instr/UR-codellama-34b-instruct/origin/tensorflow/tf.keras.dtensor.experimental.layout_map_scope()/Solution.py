
import tensorflow as tf

# Define a custom layout for the variables
layout = tf.keras.layers.Lambda(lambda x: x, output_shape=lambda s: [s[1], s[2] * 2])

with tf.variable_scope('my_model', layout=layout):
    # Create some variables within the scope
    v1 = tf.Variable(initial_value=tf.zeros([3, 4]))
    v2 = tf.Variable(initial_value=tf.ones([5, 6]))
    v3 = tf.Variable(initial_value=tf.random_normal([7, 8], mean=0.0, stddev=1.0))

# Access the variables outside of the scope and print their shapes
print(v1.shape)  # [3, 4]
print(v2.shape)  # [5, 6]
print(v3.shape)  # [7, 8]
