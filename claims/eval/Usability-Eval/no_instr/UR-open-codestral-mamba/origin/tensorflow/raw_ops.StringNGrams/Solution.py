import tensorflow as tf

# Define a list of strings
string_list = tf.constant(["Hello world", "Hi there", "This is a test"])

# Define the size of n-grams
n = 3

def create_ngrams(string_list, n):
    # Split the strings into words
    words = tf.strings.split(string_list)

    # Create a dataset with dynamic padding from the list of words
    dataset = tf.data.Dataset.from_tensor_slices(words)
    dataset = dataset.padded_batch(len(string_list), padded_shapes=(None,))

    # Create n-grams
    ngrams = dataset.skip(n-1).interleave(
        lambda x_batch: tf.data.Dataset.range(
            tf.shape(x_batch)[0] - n + 1
        ).map(
            lambda i: x_batch[i:i+n]
        )
    )

    ngrams = ngrams.map(lambda x: tf.strings.join(x, separator=" ")).batch(len(string_list))

    return ngrams

ngrams = create_ngrams(string_list, n)

# Print the n-grams
for ngram in ngrams:
    print(ngram.numpy())
