# Import tensorflow library
import tensorflow as tf

# Define the function to compute gradient of FractionalAvgPool
def fractional_avg_pool_grad(orig_input_tensor, orig_output_tensor, out_backprop,POOLsty=key, OVERLAPsty=key):
    with tf.compat.v1.Graph().as_default():
        # Original input tensor shape
        orig_input_tensor_shape = tf.shape(orig_input_tensor)
        
        # Reshape out_backprop to have same rank as original input tensor if necessary.
        out_backprop = tf.reshape(out_backprop, tf.shape(orig_input_tensor))

        row_pooling_kernel = POOLsty*tf.ones([POOLsty])
        col_pooling_kernel = POOLsty*tf.ones([POOLsty])
        op = tf.raw_ops.FractionalAvgPoolGrad(
                orig_input_tensor=orig_input_tensor,
                orig_output_tensor=orig_output_tensor,
                out_backprop=out_backprop,
                row_pooling_kernel=row_pooling_kernel,
                col_pooling_kernel=col_pooling_kernel,
                pooling_ratio=2,
                pseudorandom=None,
                deterministic=False,
                seed=0,
                seed2=0)
        
        grad = tf.reshape(op, orig_input_tensor_shape)
        
    return grad

# Example usage
if __name__ == "__main__":
    # Define variables for example usage
    input_tensor = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    output_tensor = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    backprop = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

    # Call function and print result
    print(fractional_avg_pool_grad(input_tensor, output_tensor, backprop))
