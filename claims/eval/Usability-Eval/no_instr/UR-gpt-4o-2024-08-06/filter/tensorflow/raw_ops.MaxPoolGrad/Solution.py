import tensorflow as tf

# Create a simple max pooling operation
input_shape = (1, 4, 4, 1)  # shape: (batch_size, height, width, channels)
input_data = tf.constant([[[
    [1.0], [2.0], [3.0], [4.0],
    [5.0], [6.0], [7.0], [8.0],
    [9.0], [10.0], [11.0], [12.0],
    [13.0], [14.0], [15.0], [16.0]
]]], dtype=tf.float32)

# Define a 2x2 max pooling layer with a stride of 2
pool_size = (2, 2)
strides = (2, 2)
max_pool = tf.nn.max_pool2d(input_data, ksize=pool_size, strides=strides, padding='VALID')

# Compute the gradient of max pooling
with tf.GradientTape() as tape:
    tape.watch(input_data)
    max_pool = tf.nn.max_pool2d(input_data, ksize=pool_size, strides=strides, padding='VALID')
    loss = tf.reduce_sum(max_pool)

gradients = tape.gradient(loss, input_data)

# Output the max pooled result and its gradients
print("Max pooled result:\n", max_pool.numpy())
print("Gradients with respect to the input:\n", gradients.numpy())
