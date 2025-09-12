import tensorflow as tf

def encode_tensor_to_unicode(int_tensor):
    # Ensure the input tensor is of integer type
    int_tensor = tf.convert_to_tensor(int_tensor, dtype=tf.int32)
    
    # Encode the tensor of ints into unicode strings
    unicode_tensor = tf.strings.as_string(int_tensor)

    return unicode_tensor

# Example usage
int_tensor = [65, 66, 67]  # Corresponds to 'A', 'B', 'C'
unicode_tensor = encode_tensor_to_unicode(int_tensor)
print(unicode_tensor.numpy())
