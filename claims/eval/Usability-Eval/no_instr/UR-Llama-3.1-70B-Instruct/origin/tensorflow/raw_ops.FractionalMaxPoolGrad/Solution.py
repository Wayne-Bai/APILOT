# Import necessary libraries
import tensorflow as tf

# Define the function to compute the gradient of FractionalMaxPool
def fractional_max_pool_grad(orig_input, orig_output, out_backprop, 
                              pooling_ratio, pseudo_random, 
                              overlapping, deterministic):

    # Compute the gradient of FractionalMaxPool
    gradients = tf.raw_ops.FractionalMaxPoolGrad(orig_input, 
                                                orig_output, 
                                                out_backprop, 
                                                pooling_ratio, 
                                                pseudo_random, 
                                                overlapping, 
                                                deterministic)

    return gradients


# Example usage:
if __name__ == "__main__":
    # Define the dimensions
    batch_size = 1
    input_height = 10
    input_width = 10
    channels = 1

    # Define the input, output and output backprop
    orig_input = tf.ones((batch_size, input_height, input_width, channels))
    orig_output = tf.ones((batch_size, input_height//2, input_width//2, channels))
    out_backprop = tf.ones((batch_size, input_height//2, input_width//2, channels))

    # Define the other parameters
    pooling_ratio = [1.0, 1.4333, 1.8666, 1.9047]
    pseudo_random = False
    overlapping = True
    deterministic = True

    # Compute the gradient
    gradients = fractional_max_pool_grad(orig_input, orig_output, out_backprop, 
                                         pooling_ratio, pseudo_random, 
                                         overlapping, deterministic)
    
    print(gradients)
