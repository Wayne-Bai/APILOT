import tensorflow as tf

def create_ngrams(data, n):
  # Convert the data to ragged tensor
  ragged_data = tf.ragged.constant(data)

  # Create ngrams from the ragged tensor
  ngrams = tf.strings.ngrams(ragged_data, n, separator=' ')

  return ngrams

# Example usage
data = ['TensorFlow is great', 'I love learning with TensorFlow']
n = 2
print(create_ngrams(data, n).to_list())
