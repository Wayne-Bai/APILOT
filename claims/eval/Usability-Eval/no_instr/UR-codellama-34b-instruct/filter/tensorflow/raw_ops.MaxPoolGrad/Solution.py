
import tensorflow as tf

def compute_gradients(inputs, pool_size, strides, padding):
    # Pad the input if necessary
    if padding == 'SAME':
        inputs = tf.pad(inputs, [[0, 0], [pool_size - 1, pool_size - 1], [pool_size - 1, pool_size - 1], [0, 0]])
    
    # Compute the gradients of the maxpooling function using the gradient ops
    output = tf.gradients(inputs, pool_size, strides, padding)
    
    return output
