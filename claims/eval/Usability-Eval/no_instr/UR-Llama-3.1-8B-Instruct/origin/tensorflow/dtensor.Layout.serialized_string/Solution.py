# Importing the necessary TensorFlow module
import tensorflow as tf

# Creating an example Protocol Buffers message using TensorFlow's graph_util functionality
message = tf.train.Example(
    features=tf.train.Features(
        feature={
            'int_feature': tf.train.Feature(int64_list=tf.train.Int64List(value=[1, 2, 3])),
            'float_feature': tf.train.Feature(float_list=tf.train.FloatList(value=[1.0, 2.0, 3.0]))
        }
    )
)

# Using the serializeToString() method of the message to get the serialized binary string
serialized_message = message.SerializeToString()

print(serialized_message)
