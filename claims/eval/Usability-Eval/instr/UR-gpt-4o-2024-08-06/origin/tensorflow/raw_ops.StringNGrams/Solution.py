import tensorflow as tf

# Sample ragged tensor input: a batch of sentences split into words
input_data = tf.ragged.constant([
    ['the', 'quick', 'brown', 'fox'],
    ['jumps', 'over', 'the', 'lazy', 'dog'],
    ['tensorflow', 'is', 'cool']
])

# Define the n-gram parameters
n = 2  # bi-grams
separator = " "  # separator used between words to form n-gram
 
# Use tf.strings.ngrams to create n-grams from the ragged tensor input
ngrams = tf.strings.ngrams(input_data, ngram_width=(n,), separator=separator, pad_values=None)

# Print the generated n-grams
for i, sentence_ngrams in enumerate(ngrams):
    print(f"Sentence {i+1} ngrams: {sentence_ngrams.to_list()}")
