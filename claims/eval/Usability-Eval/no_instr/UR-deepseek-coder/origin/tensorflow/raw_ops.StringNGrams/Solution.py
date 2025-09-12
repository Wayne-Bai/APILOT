import tensorflow as tf

def create_ngrams_from_ragged_string_data(ragged_strings, ngram_width):
    # Convert ragged strings to a dense tensor with padding
    dense_strings = ragged_strings.to_tensor(default_value='')
    
    # Create ngrams using tf.strings.ngrams
    ngrams = tf.strings.ngrams(dense_strings, ngram_width, separator='')
    
    # Convert the ngrams back to a ragged tensor
    ragged_ngrams = tf.RaggedTensor.from_tensor(ngrams)
    
    return ragged_ngrams

# Example usage:
ragged_strings = tf.ragged.constant([['hello', 'world'], ['tensorflow', 'is', 'great']])
ngram_width = 2

ngrams = create_ngrams_from_ragged_string_data(ragged_strings, ngram_width)
print(ngrams)
