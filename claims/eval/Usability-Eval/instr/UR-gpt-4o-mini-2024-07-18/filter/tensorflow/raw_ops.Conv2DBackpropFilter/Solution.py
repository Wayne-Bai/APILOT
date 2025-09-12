import tensorflow as tf

def compute_conv_gradients(inputs, filters, grads, strides, padding):
    # Compute the gradients of convolution with respect to the filters
    with tf.GradientTape() as tape:
        tape.watch(filters)
        conv_output = tf.nn.conv2d(inputs, filters, strides=strides, padding=padding)
    
    # Get gradients
    gradients = tape.gradient(conv_output, filters, output_gradients=grads)
    return gradients

# Example usage
inputs = tf.random.normal([1, 28, 28, 3])  # Batch of images, e.g., 1 image of size 28x28 with 3 channels
filters = tf.random.normal([3, 3, 3, 16])  # A convolutional filter of size 3x3 with 16 output channels
grads = tf.random.normal([1, 26, 26, 16])  # Gradients from the next layer
strides = [1, 1, 1, 1]  # Stride of [1, 1, 1, 1]
padding = 'VALID'  # Input size will be reduced

# Calculate gradients with respect to the filter
filter_gradients = compute_conv_gradients(inputs, filters, grads, strides, padding)
print(filter_gradients)
