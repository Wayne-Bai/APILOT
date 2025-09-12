
import tensorflow as tf

# Create a tensor of ints
input_tensor = tf.constant([10, 20, 30])

# Use tf.raw_ops.EncodeWideVocab to encode the ints into unicode strings
encoded_strings = tf.raw_ops.EncodeWideVocab(
    input=input_tensor, vocab_size=5, width=4
)

# Print the encoded strings
print(encoded_strings)
