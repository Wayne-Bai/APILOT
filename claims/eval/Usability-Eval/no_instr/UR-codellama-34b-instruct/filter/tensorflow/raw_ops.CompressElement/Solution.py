
import tensorflow as tf

# Load the dataset
dataset = tf.data.TFRecordDataset("path/to/dataset")

# Define the compression type and level
compression_type = "GZIP"
level = 5

# Apply compression to the dataset
dataset = dataset.map(lambda x: tf.raw_ops.CompressDatasetElement(inputs=[x], compression_type=compression_type, level=level))
