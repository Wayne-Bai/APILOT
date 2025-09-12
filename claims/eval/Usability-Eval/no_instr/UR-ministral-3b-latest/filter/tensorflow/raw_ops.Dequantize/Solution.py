import tensorflow as tf

# Define the method for dequantizing input tensor
def dequantize(input_tensor, scale, zero_point):
    # Function using the TensorFlow method to dequantize tensor
    input_tensor = tf.raw_ops.Dequantize(input_tensor=input_tensor,
                                          scale=scale,
                                          zero_point=zero_point,
                                          data_type=tf.float32)

    return input_tensor
