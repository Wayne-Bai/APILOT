import tensorflow as tf

def raw_to_numeric(input_tensor):
    return tf.strided_slice(input_tensor, [0, 0], [-1, -1], [1, 1])

# Example usage:
raw_bytes = tf.constant([b'\x00\x01\x02\x03', b'\x04\x05\x06\x07'], dtype=tf.string)
numeric_tensors = raw_to_numeric(raw_bytes)
print(numeric_tensors)
