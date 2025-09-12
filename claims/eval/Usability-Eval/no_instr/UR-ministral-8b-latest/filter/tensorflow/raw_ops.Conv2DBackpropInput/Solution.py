import tensorflow as tf

def compute_gradients(input_tensor, filter_tensor):
    # Extract the input and filter dimensions
    input_shape = input_tensor.shape.as_list()
    filter_shape = filter_tensor.shape.as_list()

    # Compute the convolution operation
    outputs = tf.nn.conv2d(
        input=input_tensor,
        filters=filter_tensor,
        strides=[1, 1, 1, 1],  # Assuming a stride of 1
        padding='VALID'   # Or 'SAME' depending on your application
    )

    # Compute the gradients of the output with respect to the input
    gradients_output = tf.gradients(outputs, input_tensor)

    return gradients_output

# Example usage
input_tensor = tf.constant([[[-1, -2], [-3, -4]], [[1, 2], [3, 4]]], dtype=tf.float32)
filter_tensor = tf.constant([[[1, 0], [0, -1]], [[1, 0], [0, -1]]], dtype=tf.float32)

# Compute gradients
gradients = compute_gradients(input_tensor, filter_tensor)
