import tensorflow as tf

# Assume we have a tensor
tensor = tf.random.normal([100, 100])

# Compress the tensor
compressed_tensor = tf.io.encode_compressed(tensor, 'GZIP')

# If you want to decompress the tensor
original_tensor = tf.io.decode_compressed(compressed_tensor, 'GZIP')
