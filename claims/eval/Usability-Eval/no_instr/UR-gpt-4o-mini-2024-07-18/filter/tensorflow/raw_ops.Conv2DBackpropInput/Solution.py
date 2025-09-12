import tensorflow as tf

def compute_conv_gradients(inputs, filter, conv_output_grads, strides, padding):
    # Compute gradients of convolution with respect to the input
    input_gradients = tf.raw_ops.Conv2DBackpropInput(
        input_sizes=tf.shape(inputs),
        filters=filter,
        out_backprop=conv_output_grads,
        strides=strides,
        padding=padding
    )
    return input_gradients

# Example usage
inputs = tf.random.normal([1, 28, 28, 1])  # Example input
filter = tf.random.normal([3, 3, 1, 1])  # Example filter
conv_output_grads = tf.random.normal([1, 26, 26, 1])  # Example gradients from conv output
strides = [1, 1, 1, 1]  # Strides for convolution
padding = 'VALID'  # Padding type

# Compute gradients
gradients = compute_conv_gradients(inputs, filter, conv_output_grads, strides, padding)
print(gradients)
