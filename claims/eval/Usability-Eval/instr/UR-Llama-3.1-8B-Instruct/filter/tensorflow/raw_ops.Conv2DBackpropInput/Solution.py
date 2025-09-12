# Import the tensorflow module
import tensorflow as tf

# Create a simple convolution operation
input_tensor = tf.constant([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]])
filter_tensor = tf.constant([[[[0.1, 0.2, 0.3]]]])

conv_result = tf.nn.conv2d(input_tensor, filter_tensor, 
                           strides=[1, 1, 1, 1], padding='VALID', 
                           dilation_rate=[1, 1], use_cudnn_on_gpu=None)

# Compute the gradients of the convolution operation
grad_input = tf.gradients(conv_result, input_tensor)

# Print the gradients
print("Gradients of the convolution operation:")
print(grad_input)
