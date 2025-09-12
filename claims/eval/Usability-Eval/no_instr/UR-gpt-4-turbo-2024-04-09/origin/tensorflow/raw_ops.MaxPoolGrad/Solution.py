import tensorflow as tf

def max_pooling_gradients(input_tensor, ksize, strides, padding):
    # Perform max pooling
    pooled, argmax = tf.nn.max_pool_with_argmax(
        input_tensor, ksize=ksize, strides=strides, padding=padding, include_batch_in_index=True)
    
    # Create gradient tensor with the initial shape of input
    grad = tf.gradients(pooled, input_tensor)

    return pooled, grad

# Example usage
input_tensor = tf.random.normal([1, 10, 10, 3])  # Input tensor of rank 4
ksize = [1, 2, 2, 1]
strides = [1, 2, 2, 1]
padding = 'VALID'

pooled_output, gradients = max_pooling_gradients(input_tensor, ksize, strides, padding)

# To run and get output you would use a TensorFlow session in TensorFlow 1.x
# Print the outputs
print("Pooled Output:\n", pooled_output)
print("Gradients:\n", gradients)
