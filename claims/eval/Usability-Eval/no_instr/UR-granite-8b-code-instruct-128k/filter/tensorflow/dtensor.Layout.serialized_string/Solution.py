import tensorflow as tf

# Define your message
message = tf.train.Int64List(value=[1, 2, 3])

# Serialize your message
serialized_message = message.SerializeToString()

# Print the serialized message
print(serialized_message)
