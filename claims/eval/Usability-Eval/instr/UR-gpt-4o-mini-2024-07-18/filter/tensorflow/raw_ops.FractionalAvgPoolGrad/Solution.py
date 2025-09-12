import tensorflow as tf

def fractional_avg_pool_grad(inputs, pool_size, strides, layout="NHWC", name=None):
    # Input validation
    inputs_shape = tf.shape(inputs)
    
    # Compute the gradient using tf.nn.avg_pool
    grad = tf.nn.avg_pool(inputs, ksize=pool_size, strides=strides, padding='VALID', data_format=layout)
    
    return grad

# Example usage
inputs = tf.random.uniform((1, 10, 10, 1))  # Example input tensor
pool_size = [1, 2, 2, 1]
strides = [1, 2, 2, 1]

grad = fractional_avg_pool_grad(inputs, pool_size, strides)
print(grad)
