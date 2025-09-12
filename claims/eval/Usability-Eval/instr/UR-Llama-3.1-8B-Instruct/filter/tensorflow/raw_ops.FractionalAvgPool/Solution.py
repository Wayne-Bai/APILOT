import tensorflow as tf
import numpy as np

# Create a sample input tensor
# Input should be 4D with shape [batch, in_height, in_width, channels]
input_tensor = tf.random.normal([1, 28, 28, 1])

# Define the pooling size
pooling_size = tf.Variable([2, 2])

# Define the fractional striding, for example: [0.5, 0.5]
fractional_strides = tf.constant([0.5, 0.5])

# Create a sessoin
with tf.Session() as sess:
    # Initialize all variables
    sess.run(tf.global_variables_initializer())
    
    # Get the pooling size value
    pool_height = int(pooling_size.value()[0])
    pool_width = int(pooling_size.value()[1])
    
    # Calculate the input size divided by pooling size
    left = tf.floor(pooling_size * fractional_strides)[0]
    right = tf.ceil(tf.add(input_tensor.shape[1], tf.negative(pooling_size * fractional_strides)))[0]

    # Perform fractional average pooling
    start_x = tf.cast(tf.maximum(0, tf.cast(tf.cast(input_tensor.shape[1], tf.float32) -
                                             tf.cast(right, tf.float32), tf.int32)),
                      tf.int32)
    end_x = tf.cast(tf.minimum(tf.cast(input_tensor.shape[1], tf.int32),
                                tf.cast(tf.cast(input_tensor.shape[1], tf.float32) - 
                                         tf.cast(left, tf.float32) + 1, tf.int32)),
                    tf.int32)
    start_y = tf.cast(tf.maximum(0, tf.cast(tf.cast(input_tensor.shape[2], tf.float32) -
                                             tf.cast(right, tf.float32), tf.int32)),
                      tf.int32)
    end_y = tf.cast(tf.minimum(tf.cast(input_tensor.shape[2], tf.int32),
                                tf.cast(tf.cast(input_tensor.shape[2], tf.float32) - 
                                         tf.cast(left, tf.float32) + 1, tf.int32)),
                    tf.int32)
    
    average_pool = tf.reduce_mean(input_tensor[:, start_y:end_y, start_x:end_x, :], [1, 2])
    
    # Print the output
    print(sess.run(average_pool))
