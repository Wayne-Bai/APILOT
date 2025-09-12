import tensorflow as tf

# Define a sample Protobuf message
message = tf.train.Example()
message.features.feature['foo'].bytes_list.value.append(b'bar')

# Serialize the message to a binary string
serialized_message = message.SerializeToString()

# Print the serialized message
print(serialized_message)
