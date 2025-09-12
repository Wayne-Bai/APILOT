import tensorflow as tf

def create_ngrams_from_ragged_string_data(ragged_strings, ngram_width):
    # Convert ragged strings to a dense tensor with padding
    dense_strings = ragged_strings.to_tensor(default_value='')
    
    # Create a list to hold the ngrams
    ngrams_list = []
    
    # Iterate over each string in the dense tensor
    for string in dense_strings:
        # Split the string into words
        words = tf.strings.split([string]).values
        
        # Create ngrams from the words
        ngrams = tf.data.Dataset.from_tensor_slices(words).window(ngram_width, shift=1, drop_remainder=True)
        ngrams = ngrams.flat_map(lambda window: window.batch(ngram_width))
        ngrams = ngrams.map(lambda window: tf.strings.reduce_join(window, separator=' '))
        
        # Collect the ngrams into a list
        ngrams_list.append(tf.reshape(list(ngrams), [-1]))
    
    # Convert the list of ngrams back to a ragged tensor
    ragged_ngrams = tf.ragged.constant(ngrams_list)
    
    return ragged_ngrams

# Example usage:
ragged_strings = tf.ragged.constant([['hello world'], ['tensorflow is great'], ['ngrams']])
ngram_width = 2
ngrams = create_ngrams_from_ragged_string_data(ragged_strings, ngram_width)
print(ngrams)
