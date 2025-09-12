import tensorflow as tf

# Example of using gradient with respect to the input using conv2d
def conv2d_input_gradient(input_shape, filter_shape, output_grad_shape):
    # Create random tensors simulating inputs and filters
    input_tensor = tf.random.normal(input_shape)
    filter_tensor = tf.random.normal(filter_shape)

    # Perform convolution
    output_tensor = tf.nn.conv2d(input_tensor, filter_tensor, strides=[1, 1, 1, 1], padding='SAME')

    # Dummy gradient to backpropagate
    output_grad = tf.random.normal(output_grad_shape)

    # Compute gradients of input using TensorFlow gradient tape
    with tf.GradientTape() as tape:
        tape.watch(input_tensor)
        output_tensor = tf.nn.conv2d(input_tensor, filter_tensor, strides=[1, 1, 1, 1], padding='SAME')
        
    # Get the gradient of the input
    input_grad = tape.gradient(output_tensor, input_tensor, output_gradients=output_grad)
    
    return input_grad

# Example shapes
input_shape = (1, 10, 10, 3)      # [batch_size, height, width, channels]
filter_shape = (3, 3, 3, 8)       # [filter_height, filter_width, in_channels, out_channels]
output_grad_shape = (1, 10, 10, 8) # Must match the output shape of the conv2d operation

# Get the gradient with respect to the input
grads = conv2d_input_gradient(input_shape, filter_shape, output_grad_shape)
print(grads)
