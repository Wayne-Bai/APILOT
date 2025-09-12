import tensorflow as tf
from tensorflow.io import decode_gzip

# Load the compressed data from a file
with open('data.gz', 'rb') as f:
    data = f.read()

# Uncompress the data using GZip compression
uncompressed_data = tf.raw_ops.GUnzip(input=data)

# Get the uncompressed data as a numpy array
result = np.frombuffer(uncompressed_data, dtype=np.uint8)

print(result)
