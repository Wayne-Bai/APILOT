import tensorflow as tf

def greedy_decoding(logits):
    follicle, _ = tf.raw_ops.GreedyDecode(class_logits=logits)
    return follicle

# Example usage:
logits = tf.constant([[0.1, 0.2, 0.7], [0.5, 0.3, 0.2]])
decoded_classes = greedy_decoding(logits)
print(decoded_classes)  # Output will be the indices of the highest logits in each row
