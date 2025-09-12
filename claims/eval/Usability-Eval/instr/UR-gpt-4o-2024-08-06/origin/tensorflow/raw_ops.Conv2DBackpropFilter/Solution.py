import tensorflow as tf

# Function to compute gradients of convolution with respect to the filter
def conv2d_filter_gradients(input_tensor, filter_shape, out_backprop, strides, padding):
    # Compute input_shape from the input_tensor
    input_shape = tf.shape(input_tensor)
    
    # Convert the filter_shape to a tf.Tensor if it is not
    filter_shape_tensor = tf.constant(filter_shape, dtype=tf.int32)
    
    # Estimate the filter gradients using the Conv2DBackpropFilterV2 operation
    filter_gradients = tf.nn.conv2d_backprop_filter(
        input=input_tensor,
        filter_sizes=filter_shape_tensor,
        out_backprop=out_backprop,
        strides=strides,
        padding=padding
    )
    
    return filter_gradients

# Example usage
input_tensor = tf.random.normal(shape=(1, 5, 5, 1))  # Single grayscale image with height and width of 5
filter_shape = [3, 3, 1, 1]  # A 3x3 filter
output_gradient = tf.random.normal(shape=(1, 3, 3, 1))  # Gradient of output w.r.t some loss
strides = [1, 1, 1, 1]
padding = 'VALID'

# Compute the filter gradient
filter_gradient_result = conv2d_filter_gradients(input_tensor, filter_shape, output_gradient, strides, padding)

# Launch a session to compute the result
with tf.Session() as sess:
    result = sess.run(filter_gradient_result)
    print("Filter Gradients:")
    print(result)
