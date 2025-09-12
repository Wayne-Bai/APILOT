import tensorflow as tf

# Create a tensor of integers
int_tensor = tf.constant([123, 456, 789])

# Encode the tensor of integers to Unicode strings
string_tensor = tf.strings.as_string(int_tensor)

# Print the results
with tf.Session() as sess:
    print(sess.run(string_tensor))
