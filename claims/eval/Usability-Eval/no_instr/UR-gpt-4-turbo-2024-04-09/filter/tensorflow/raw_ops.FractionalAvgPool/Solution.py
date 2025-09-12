import tensorflow as tf

def fractional_avg_pool(input_tensor, pooling_ratio):
    """
    Perform fractional average pooling on the input tensor using TensorFlow.
    
    Args:
    input_tensor : tf.Tensor
        The input tensor to perform pooling on.
    pooling_ratio : list of floats
        Downsampling factor for each dimension.
    """
    output, _ = tf.raw_ops.FractionalAvgPool(
        value=input_tensor,
        pooling_ratio=pooling_ratio,
        pseudo_random=False,
        overlapping=False,
        deterministic=False,
        seed=0,
        seed2=0
    )
    return output

# Example usage
input_tensor = tf.random.normal([1, 8, 8, 3])  # Example shape: batch_size, height, width, channels
pooling_ratio = [1.0, 1.44, 1.44, 1.0]  # Example pooling ratio

output_tensor = fractional_avg_pool(input_tensor, pooling_ratio)
print(output_tensor.shape)  # Output shape after fractional pooling
