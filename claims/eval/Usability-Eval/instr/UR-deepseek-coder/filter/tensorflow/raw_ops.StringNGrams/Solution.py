import tensorflow as tf

def create_ngrams_from_ragged_string_data(ragged_tensor, ngram_width, separator=""):
    # Convert ragged tensor to a dense tensor
    dense_tensor = ragged_tensor.to_tensor(default_value="")
    
    # Split the strings into tokens
    tokens = tf.strings.split(dense_tensor, sep=" ")
    
    # Create ngrams
    ngrams = tf.strings.ngrams(tokens, ngram_width, separator=separator)
    
    # Convert ngrams back to ragged tensor
    ragged_ngrams = tf.RaggedTensor.from_tensor(ngrams)
    
    return ragged_ngrams

# Example usage
ragged_tensor = tf.ragged.constant([["hello", "world"], ["tensorflow", "is", "great"]])
ngram_width = 2
separator = " "

ngrams = create_ngrams_from_ragged_string_data(ragged_tensor, ngram_width, separator)
print(ngrams)
