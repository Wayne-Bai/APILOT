import tensorflow as tf

# Create a variable
x = tf.Variable(5)

# Serialize the variable to a Protobuf binary string
serializer = tf.compat.v1.train.Saver()
serialized_str = serializer.save(sess=None, dir="/tmp/my_model", global_step=None)

# Print the serialized string
print(serialized_str)