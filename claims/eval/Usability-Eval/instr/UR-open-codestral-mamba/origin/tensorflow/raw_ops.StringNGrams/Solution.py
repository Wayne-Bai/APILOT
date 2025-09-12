import tensorflow as tf
from tensorflow.python.ops import string_ops

def create_ngrams(input_tensor, n):
    # Pad the input tensor with empty strings
    padded_tensor = string_ops.pad(input_tensor, [[0, 0], [0, n-1]], "CONSTANT")

    # Create sliding windows of size n along the second axis
    ngrams = tf.constant([padded_tensor[:, i:i+n] for i in range(padded_tensor.shape[1]-n+1)])

    # Collapse the axis to get the final n-grams tensor
    ngrams_tensor = tf.reshape(ngrams, [-1, n])

    return ngrams_tensor

# Example usage
input_tensor = tf.constant([['I', 'love', 'to'], ['write', 'code', 'in'], ['Python', 'and', 'TensorFlow']])
n = 3
ngrams_tensor = create_ngrams(input_tensor, n)
print(ngrams_tensor.numpy())
