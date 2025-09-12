
import tensorflow as tf

# Define a function to decode raw bytes into numeric tensors
def decode_raw(input_tensor):
    decoded_tensor = tf.io.decode_raw(input_tensor, out_type=tf.float32)
    
    return decoded_tensor
