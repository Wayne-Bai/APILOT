import tensorflow as tf

def bytes_to_numeric_tensors(raw_bytes):
    # Decode the raw bytes into a tensor
    decoded = tf.io.decode_raw(raw_bytes, out_type=tf.float32, little_endian=True)

    # Reshape according to your requirements, for example, if you know they're 1D vectors of length 100:
    # decoded = tf.reshape(decoded, [-1, 100])

    return decoded
