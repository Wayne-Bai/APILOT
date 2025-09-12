import tensorflow as tf

def fractional_avg_pool(input_tensor, pooling_ratio, pseudo_random=False, overlapping=False, seeded=False, seed=0):
    """
    Performs fractional average pooling on the input.

    Args:
        input_tensor (tf.Tensor): The input tensor.
        pooling_ratio (list of float): Pooling ratio for each dimension of input.
        pseudo_random (bool): Whether to use a pseudorandom seed.
        overlapping (bool): Whether to have overlapping pooling.
        seeded (bool): If True, use 'seed' to seed the random number generator.
        seed (int): Random seed.

    Returns:
        tf.Tensor: The pooled tensor.
    """
    if seeded:
        tf.random.set_seed(seed)

    output, _ = tf.nn.fractional_avg_pool(
        input_tensor, 
        pooling_ratio=pooling_ratio, 
        pseudo_random=pseudo_random, 
        overlapping=overlapping
    )
    
    return output

# Example usage
input_data = tf.constant([[
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
]], dtype=tf.float32)

pooling_ratio = [1.0, 1.5, 1.5]  # Assuming a 3x3 input being reduced

pooled_output = fractional_avg_pool(input_data, pooling_ratio)
print("Pooled Output:", pooled_output.numpy())
