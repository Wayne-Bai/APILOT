import tensorflow as tf
from tensorflow_datasets import load

# Load a dataset using TensorFlow Datasets
dataset = load('mnist', split='train')

# Serialize the dataset into a Protobuf binary string representation
serialized_proto = tf.io.serialize_proto(dataset)

print(serialized_proto)
