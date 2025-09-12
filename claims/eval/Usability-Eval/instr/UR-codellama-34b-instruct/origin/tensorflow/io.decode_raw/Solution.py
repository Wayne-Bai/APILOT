import tensorflow as tf

def convert_raw_to_numeric(input_tensor):
    # Use `tf.io.decode_raw` to convert raw bytes to numeric tensors
    decoded_bytes = tf.io.decode_raw(input_tensor, out_type=tf.float32)
    return decoded_bytes
