import tensorflow as tf

def int_to_unicode(input_tensor):
    return tf.strings.unicode_decode(input_tensor)

# Example usage:
input_tensor = tf.constant([72, 101, 108, 108, 111])  # ASCII values for 'Hello'
output_tensor = int_to_unicode(input_tensor)
print(output_tensor.numpy().decode('utf-8'))  # Output: 'Hello'
