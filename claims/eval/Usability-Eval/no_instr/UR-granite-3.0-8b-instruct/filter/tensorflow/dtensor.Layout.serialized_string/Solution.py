import tensorflow as tf

# Assuming 'data' is a TensorFlow tensor containing the data you want to serialize
# Replace 'YourDataType' with the actual data type of your tensor
data = tf.constant([1, 2, 3], dtype='YourDataType')

# Serialize the tensor to a binary string
serialized_data = tf.io.serialize_tensor(data).numpy().tobytes()

print(serialized_data)
