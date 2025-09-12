import tensorflow as tf

def encode_ints_to_unicode_strings(input_tensor):
    # Convert each integer in the input tensor to a Unicode character
    unicode_chars = tf.strings.unicode_encode(input_tensor, output_encoding='UTF-8')
    
    # Join the Unicode characters into a single string
    encoded_string = tf.strings.reduce_join(unicode_chars, separator='')
    
    return encoded_string

# Example usage:
input_tensor = tf.constant([72, 101, 108, 108, 111])  # Corresponds to 'Hello'
result = encode_ints_to_unicode_strings(input_tensor)
print(result.numpy().decode('utf-8'))  # Output: 'Hello'
