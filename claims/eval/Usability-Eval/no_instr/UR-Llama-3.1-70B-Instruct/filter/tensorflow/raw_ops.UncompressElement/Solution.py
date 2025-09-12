import tensorflow as tf

def uncompress_element(compressed, compression_type, name=None):
    return tf.raw_ops.UncompressElement(compressed=compressed, compression_type=compression_type, name=name)

# Example usage:
compressed_data = tf.constant([255, 216, 255, 219, 255, 219], dtype=tf.uint8)
compression_type = tf.string

result = uncompress_element(compressed_data, compression_type)

print(result)

# Note:
# For more accurate result use Session to Run the output
with tf.compat.v1.Session() as sess:
  print(sess.run(result))
  
# Output result:
