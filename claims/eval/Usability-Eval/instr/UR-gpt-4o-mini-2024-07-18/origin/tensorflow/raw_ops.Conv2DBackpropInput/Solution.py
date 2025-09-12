import tensorflow as tf

# Function to compute gradients of convolution with respect to input
def compute_conv_grad(input_tensor, filters, strides, padding):
    with tf.GradientTape() as tape:
        tape.watch(input_tensor)
        convolution_output = tf.nn.conv2d(input_tensor, filters, strides=strides, padding=padding)
    
    # Compute gradients
    gradients = tape.gradient(convolution_output, input_tensor)
    return gradients

# Example usage
input_tensor = tf.random.normal([1, 28, 28, 1])  # Example input
filters = tf.random.normal([3, 3, 1, 16])         # Example filter
strides = [1, 1, 1, 1]                             # Strides
padding = "SAME"                                   # Padding

gradients = compute_conv_grad(input_tensor, filters, strides, padding)
print(gradients)
