import tensorflow as tf

# Define a tensor containing integers
tensor = tf.constant([1, 2, 3, 4])

# Convert each entry in the tensor to a string
string_tensor = tf.py_func(lambda x: str(x), [tensor], tf.string)

print(string_tensor)
