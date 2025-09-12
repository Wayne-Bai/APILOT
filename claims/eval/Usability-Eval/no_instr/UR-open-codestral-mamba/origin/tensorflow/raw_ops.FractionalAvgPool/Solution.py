import tensorflow as tf

# This function performs fractional average pooling on an input tensor
def fractional_avg_pool(tensor, pool_size):
    # Define a random menas for each spatial average operation
    random_means = tf.random.uniform([tensor.shape[-1]], 0.0, 1.0, dtype=tf.float32)

    # Define a function to perform spatial average pooling
    def spatial_avg_pool(x):
        return tf.nn.avg_pool(x, pool_size, pool_size, 'VALID')

    # Define a function to perform fractional spatial average pooling
    def frac_avg_pool(x):
        # Flatten the tensor
        flat_tensor = tf.reshape(x, [-1])

        # Multiply each element by a random mean
        weighted_tensor = tf.multiply(flat_tensor, random_means)

        # Reshape the tensor back to the original shape
        reshaped_tensor = tf.reshape(weighted_tensor, x.shape)

        # Perform spatial average pooling
        pooled_tensor = spatial_avg_pool(reshaped_tensor)

        # Return the pooled tensor
        return pooled_tensor

    # Define a function to perform fractional average pooling on a single channel
    def fractional_avg_pool_single_channel(channel):
        # Perform fractional average pooling on the channel
        pooled_channel = frac_avg_pool(tf.expand_dims(channel, axis=-1))

        # Squeeze the channel to remove the extra dimension
        return tf.squeeze(pooled_channel, axis=-1)

    # Apply fractional average pooling on each channel of the tensor
    pooled_tensor = tf.stack([fractional_avg_pool_single_channel(channel) for channel in tf.unstack(tensor, axis=-1)], axis=-1)

    return pooled_tensor
