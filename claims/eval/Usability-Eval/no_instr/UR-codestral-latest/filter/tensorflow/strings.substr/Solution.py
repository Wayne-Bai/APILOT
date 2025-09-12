import tensorflow as tf

# Create a tensor of strings
strings_tensor = tf.constant(['Hello, TensorFlow', 'How are you?', 'I hope you are well'])

# Extract the first 5 characters from each string
substrings = tf.strings.substr(strings_tensor, 0, 5)

# Display the substrings
with tf.Session() as sess:
    print(sess.run(substrings))
