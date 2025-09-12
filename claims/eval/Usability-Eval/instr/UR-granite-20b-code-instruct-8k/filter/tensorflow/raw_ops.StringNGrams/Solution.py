
import tensorflow as tf

# Define the ragged string data
ragged_string_data = tf.constant(["This is a sample sentence.", "Here is another sample sentence."])

# Create ngrams from the ragged string data
ngrams = tf.raw_ops. string_ngrams(
    data=ragged_string_data,
    ngram_width=2,
    separator=" ",
    pad_string="",
    keep_whitespace=False
)

print(ngrams)
