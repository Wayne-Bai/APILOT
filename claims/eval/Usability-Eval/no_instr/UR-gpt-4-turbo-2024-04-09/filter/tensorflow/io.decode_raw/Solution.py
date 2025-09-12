import tensorflow as tf

def convert_raw_bytes_to_numeric_tensors(input_tensor):
    # Decode the raw bytes into a tensor
    numeric_tensor = tf.io.decode_raw(input_tensor, out_type=tf.float32)
    return numeric_tensor
