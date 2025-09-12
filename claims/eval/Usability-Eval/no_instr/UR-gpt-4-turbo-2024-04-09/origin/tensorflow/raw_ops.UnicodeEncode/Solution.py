import tensorflow as tf

# Define an integer tensor
int_tensor = tf.constant([67, 111, 100, 105, 110, 103])

# Encode the integer tensor into a unicode string
encoded_string = tf.strings.unicode_encode(
    input=int_tensor[tf.newaxis, :],  # add batch dimension
    input_encoding='UTF-8'
)

# Print the encoded string
tf.print(encoded_string)
