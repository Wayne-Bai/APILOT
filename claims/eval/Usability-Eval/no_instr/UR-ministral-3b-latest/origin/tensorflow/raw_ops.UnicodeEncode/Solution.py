import tensorflow as tf

# Function to encode a tensor of ints into unicode strings
def encode_tensors_to_unicode_strings(tensors):
    unicode_tensors = tf.raw_ops.EncoderInt64(target_dtype=tf.string)
    return unicode_tensors

# Example tensor
tensor_int32 = tf.constant([10, 20, 30], dtype=tf.int32)

# Encode the tensor using the method
unicode_tensors = encode_tensors_to_unicode_strings(tensor_int32)

# Print the result
print(unicode_tensors)
