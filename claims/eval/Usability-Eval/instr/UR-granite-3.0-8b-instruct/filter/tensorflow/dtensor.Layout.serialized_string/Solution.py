import tensorflow as tf

# Assuming 'data' is a tensor containing the data you want to serialize
data = tf.constant([1, 2, 3, 4, 5])

# Convert the tensor to a serialized Protobuf binary string
serialized_data = tf.io.serialize_tensor(data).numpy().decode('utf-8')

print(serialized_data)
