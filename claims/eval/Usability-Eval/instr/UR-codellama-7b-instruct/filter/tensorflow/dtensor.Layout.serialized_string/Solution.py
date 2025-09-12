
import tensorflow as tf

# Define a function that takes in a Protobuf message and returns its serialized binary string representation
def serialize_proto(msg):
    # Convert the Protobuf message to a string using TensorFlow's serialize_proto() function
    serialized = tf.keras.utils.serialize_proto(msg)
    return serialized

# Test the function by creating a Protobuf message and passing it to the function
msg = tf.example.Example()
msg.features.feature["x"].float_list.value.extend([1, 2, 3])
serialized = serialize_proto(msg)
print(serialized)
