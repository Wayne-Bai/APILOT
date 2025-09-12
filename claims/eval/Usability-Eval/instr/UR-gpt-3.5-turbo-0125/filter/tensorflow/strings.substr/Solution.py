
import tensorflow as tf

# Creating a tensor of strings
strings_tensor = tf.constant(["hello", "world", "tensorflow"])

# Substring operation to extract substrings
substring_tensor = tf.strings.substr(strings_tensor, pos=1, len=3)

# Running a TensorFlow session to get the result
with tf.Session() as sess:
    result = sess.run(substring_tensor)

print(result)
