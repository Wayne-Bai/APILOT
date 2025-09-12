import tensorflow as tf

def encode_ints_to_unicode(tensor_of_ints):
    # Convert the tensor of ints to a tensor of bytes
    tensor_of_bytes = tf.bitcast(tensor_of_ints, tf.uint8)
    
    # Encode the tensor of bytes to a tensor of unicode strings
    tensor_of_unicode = tf.strings.unicode_encode(tensor_of_bytes, 'UTF-8')
    
    return tensor_of_unicode

# Example usage:
# tensor_of_ints = tf.constant([72, 101, 108, 108, 111])  # ASCII values for "Hello"
# result = encode_ints_to_unicode(tensor_of_ints)
# print(result.numpy())  # Output: b'Hello'
