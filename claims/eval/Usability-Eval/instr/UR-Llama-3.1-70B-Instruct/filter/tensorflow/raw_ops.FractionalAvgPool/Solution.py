import tensorflow as tf

# Define a function for fractional average pooling
def fractional_avg_pool(value, pooling_ratio, pseudo_random, overlapping, deterministic, seed=0, name=None):
    with tf.name_scope(name, "FractionalAvgPool", [value]):
        # Get the input shape
        input_shape = tf.shape(value)
        
        # Calculate the batch and channels
        batch = input_shape[0]
        channels = input_shape[-1]
        
        # Calculate the output height and width
        output_height = tf.cast(tf.ceil(input_shape[1] * pooling_ratio), tf.int32)
        output_width = tf.cast(tf.ceil(input_shape[2] * pooling_ratio), tf.int32)
        
        # Calculate the output shape
        output_shape = tf.stack([batch, output_height, output_width, channels])
        
        # Perform fractional average pooling
        output = tf.raw_ops.FractionalAvgPool(
            value=value,
            pooling_ratio=pooling_ratio,
            pseudo_random=pseudo_random,
            overlapping=overlapping,
            deterministic=deterministic,
            seed=seed,
            seed2=0,
            output=output_shape
        )
        
        return output

# Usage example
# Create a random input tensor
input_tensor = tf.random.normal([1, 10, 10, 3])

# Define the pooling ratio
pooling_ratio = 0.5

# Perform fractional average pooling
output = fractional_avg_pool(
    value=input_tensor,
    pooling_ratio=pooling_ratio,
    pseudo_random=False,
    overlapping=False,
    deterministic=False,
    name="FractionalAvgPool"
)

# Print the output shape
print(output.shape)
