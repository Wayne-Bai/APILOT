import tensorflow as tf

# Assuming 'tensor' is the input tensor
string_tensor = tf.strings.format('{}', [tf.reduce_mean(tensor)])

print(string_tensor)
