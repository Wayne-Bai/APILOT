import tensorflow as tf

def encode_ints_to_unicode_strings(input_tensor):
    # Convert the input tensor of ints to a tensor of bytes
    byte_tensor = tf.strings.unicode_encode(input_tensor, 'UTF-8')
    
    # Convert the byte tensor to a tensor of unicode strings
    unicode_tensor = tf.strings.unicode_decode(byte_tensor, 'UTF-8')
    
    return unicode_tensor

# Example usage:
input_tensor = tf.constant([72, 101, 108, 108, 111])  # ASCII codes for "Hello"
result = encode_ints_to_unicode_strings(input_tensor)
print(result.numpy())
