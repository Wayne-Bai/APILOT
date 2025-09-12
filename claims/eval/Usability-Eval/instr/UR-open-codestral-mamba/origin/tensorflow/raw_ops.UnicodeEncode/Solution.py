import tensorflow as tf

# Create a TensorFlow constant tensor with integer values
input_tensor = tf.constant([65, 66, 67, 68, 69], dtype=tf.int32)

# Encode the integer values into Unicode strings using tf.raw_ops.EncodeJpeg
encoded_tensor = tf.raw_ops.Iso646Encode(input=input_tensor)

# Print the encoded tensor to verify
with tf.Session() as sess:
    print(sess.run(encoded_tensor))
