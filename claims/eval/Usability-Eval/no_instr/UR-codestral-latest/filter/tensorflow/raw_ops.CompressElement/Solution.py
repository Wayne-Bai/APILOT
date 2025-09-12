import tensorflow as tf
import numpy as np

# assuming `data` is a single data point in your dataset
data = np.random.rand(100, 100).astype(np.float32)

# encode the data to a base64 string with GZIP compression
compressed_data = tf.io.encode_base64(tf.io.gzip.GzipCompression(data))
