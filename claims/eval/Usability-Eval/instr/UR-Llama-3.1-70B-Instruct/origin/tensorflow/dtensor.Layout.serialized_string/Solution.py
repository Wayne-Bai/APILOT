import tensorflow as tf
from tensorflow.core.protobuf import saver_pb2

# Create a TensorFlow session
session = tf.Session()

# Create a TensorFlow variable
variable = tf.Variable(42, name='my_variable')

# Create a TensorFlow saver
saver = tf.train.Saver([variable])

# Initialize the variable
session.run(tf.global_variables_initializer())

# Save the variable to a binary string
serialized_binary_string = saver.export_meta_graph(filename='model.meta', as_text=False)

# Print the serialized binary string representation
print(serialized_binary_string)
