import tensorflow as tf

def fractional_average_pooling(input_tensor, pool_size, output_size):
    # Perform fractional average pooling using tf.nn.avg_pool
    pooled_tensor = tf.nn.avg_pool2d(
        input_tensor,
        ksize=[1, pool_size[0], pool_size[1], 1],
        strides=[1, pool_size[0], pool_size[1], 1],
        padding='VALID'
    )
    # Since tf.nn.avg_pool does not directly do fractional pooling,
    # we will need to manually handle the output size to simulate fractional pooling
    return tf.image.resize(pooled_tensor, output_size)

# Example usage
input_tensor = tf.random.uniform((1, 8, 8, 1))  # Batch size of 1, 8x8 image with 1 channel
pool_size = (2, 2)  # Pooling size
output_size = (4, 4)  # Desired output size after pooling

result = fractional_average_pooling(input_tensor, pool_size, output_size)
print(result)
