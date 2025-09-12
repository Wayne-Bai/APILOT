import tensorflow as tf

def fractional_average_pool(input_tensor, pooling_ratio, pseudo_random=False, overlapping=False, seed=0, seed2=0):
    # Perform fractional average pooling on the input tensor
    result = tf.nn.fractional_avg_pool(
        input_tensor,
        pooling_ratio=pooling_ratio,
        pseudo_random=pseudo_random,
        overlapping=overlapping,
        seed=seed,
        seed2=seed2
    )
    return result

# Example usage:
input_tensor = tf.constant([[[[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]]]])
pooling_ratio = [1.0, 1.5, 1.5, 1.0]
output = fractional_average_pool(input_tensor, pooling_ratio)
print(output)
