import tensorflow as tf

def fractional_avg_pool(input_tensor, pooling_ratio):
    """
    This function applies fractional average pooling on the input tensor.
    """
    pool_height, pool_width = int(input_tensor.shape[1] * pooling_ratio[0]), int(input_tensor.shape[2] * pooling_ratio[1])
    
    return tf.nn.avg_pool2d(
        input_tensor,
        ksize=[1, pool_height, pool_width, 1],
        strides=[1, pool_height, pool_width, 1],
        padding='VALID'
    )

def compute_gradient(input_tensor, pooling_ratio):
    """
    Computes the gradient of a fractional average pool with respect to the input tensor.
    """
    with tf.GradientTape() as tape:
        tape.watch(input_tensor)
        # Apply fractional avg pooling operation
        fractional_pooled = fractional_avg_pool(input_tensor, pooling_ratio)
    
    # Compute gradient of the fractional average pooling output with respect to the input
    gradient = tape.gradient(fractional_pooled, input_tensor)
    
    return gradient

# Example input tensor
input_tensor = tf.constant([
    [[1.0, 2.0], [3.0, 4.0]], 
    [[5.0, 6.0], [7.0, 8.0]]
], dtype=tf.float32)

# Reshape input_tensor to have the dimensions [batch, height, width, channels]
input_tensor = tf.reshape(input_tensor, [1, 2, 2, 2])

# Pooling ratio: fractional part of the original dimensions (as an example)
pooling_ratio = (0.5, 0.5)  # Pool by half

# Compute the gradient
gradient = compute_gradient(input_tensor, pooling_ratio)

# To demonstrate, we convert the result gradient to a numpy array for easy viewing
print("Gradient of the Fractional Avg Pool:\n", gradient.numpy())
