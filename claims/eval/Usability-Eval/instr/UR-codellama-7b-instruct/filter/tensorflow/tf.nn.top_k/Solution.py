
import tensorflow as tf

def top_k(input_tensor, k):
    # Calculate the reduced shape for the input tensor
    reduced_shape = input_tensor.get_shape()[:-1]

    # Use TensorFlow's built-in function to calculate the top k indices and values
    # for the last dimension of the input tensor
    _, topk_indices = tf.nn.top_k(tf.reshape(input_tensor, (-1,)), k)

    # Reshape the top k indices and values back to the original shape
    topk_indices = tf.reshape(topk_indices, reduced_shape + [k])

    return topk_indices
