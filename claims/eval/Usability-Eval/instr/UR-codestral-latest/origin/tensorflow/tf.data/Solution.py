import tensorflow as tf

# Assume we have a list of filenames
filenames = ["/path/to/data1.tfrecord", "/path/to/data2.tfrecord", ...]

# Create a Dataset from the filenames
dataset = tf.data.TFRecordDataset(filenames)

# Parse the records
def parse_record(record):
    features = tf.io.parse_single_example(record, features={'x': tf.io.FixedLenFeature([], tf.float32),
                                                            'y': tf.io.FixedLenFeature([], tf.int64)})
    return features['x'], features['y']

# Apply the parse function to each item in the dataset
dataset = dataset.map(parse_record)

# Shuffle and batch the data
dataset = dataset.shuffle(buffer_size=1024).batch(32)
