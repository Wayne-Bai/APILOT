
import tensorflow as tf

def greedy_decoder(logits):
    decoded_indices = tf.argmax(logits, axis=-1, output_type=tf.int32)
    return decoded_indices

# Example usage
logits = tf.constant([[0.1, 0.2, 0.7], [0.8, 0.1, 0.1]])
decoded_output = greedy_decoder(logits)
print(decoded_output)
