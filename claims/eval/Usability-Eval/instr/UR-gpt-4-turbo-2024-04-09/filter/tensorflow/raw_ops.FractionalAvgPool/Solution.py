import tensorflow as tf

def fractional_avg_pool(input_tensor, pooling_ratio, pseudo_random=False, overlapping=False, deterministic=False, seed=0, seed2=0, name=None):
    # The pooling ratio determines the scaling factor of the pooling operation
    # Shape of the input tensor (batch_size, height, width, channels)
    input_shape = tf.shape(input_tensor)
    height = tf.cast(input_shape[1], tf.float32)
    width = tf.cast(input_shape[2], tf.float32)
    
    # Calculate new height and width after applying the pooling ratio
    new_height = tf.cast(tf.math.floor(height * pooling_ratio), tf.int32)
    new_width = tf.cast(tf.math.floor(width * pooling_ratio), tf.int32)
    
    # Checking to verify that new dimensions are smaller than original
    assert_op1 = tf.Assert(tf.less(new_height, input_shape[1]), [new_height])
    assert_op2 = tf.Assert(tf.less(new_width, input_shape[2]), [new_width])
    
    with tf.control_dependencies([assert_op1, assert_op2]):
        # Creating average pooling with calculated dimensions
        pooled_tensor = tf.nn.avg_pool2d(
            input=input_tensor,
            ksize=[1, new_height, new_width, 1],
            strides=[1, new_height, new_width, 1],
            padding='VALID',
            name=name
        )
        return pooled_tensor

# Example usage 
# Creating a random tensor
input_tensor = tf.random.normal([1, 10, 10, 3])  # (batch_size, height, width, channels)
pooling_ratio = 0.5

# Call the fractional average pooling function
result_tensor = fractional_avg_pool(input_tensor, pooling_ratio)
print("Output Tensor Shape:", result_tensor.shape)
