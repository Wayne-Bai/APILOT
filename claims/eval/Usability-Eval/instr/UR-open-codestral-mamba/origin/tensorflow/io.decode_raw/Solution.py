import tensorflow as tf

def convert_raw_bytes_to_numeric(input_tensor):
    decoded_tensor = tf.decode_raw(input_tensor, out_type=tf.float32)
    return decoded_tensor
