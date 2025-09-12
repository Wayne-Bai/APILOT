import tensorflow as tf

# Define the input tensor and the maxpooling operation
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
maxpool_output = tf.raw_ops.MaxPool(input=input_tensor, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# Define the gradient function
def maxpool_grad(maxpool_output, grad_output):
    return tf.raw_ops.MaxPoolGrad(orig_input=input_tensor, grad=grad_output, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# Compute the gradients
grad_output = tf.constant([[1, 0], [0, 1]])
grad_input = maxpool_grad(maxpool_output, grad_output)

# Print the result
print(grad_input)
