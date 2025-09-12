
import tensorflow as tf
from google.protobuf import text_format

# Define a function to serialize a protobuf message to a binary string
def serialize_protobuf_message(message):
    return message.SerializeToString()

# Example usage
protobuf_message = tf.train.Example(features=tf.train.Features(feature={
    'feature_key': tf.train.Feature(int64_list=tf.train.Int64List(value=[123])),
    'another_key': tf.train.Feature(bytes_list=tf.train.BytesList(value=[b'value1', b'value2']))
}))

serialized_protobuf_string = serialize_protobuf_message(protobuf_message)
print(serialized_protobuf_string)
