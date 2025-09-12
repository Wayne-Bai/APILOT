import tensorflow as tf

def create_ngrams(strings, n):
    # Convert strings to ragged tensors
    ragged_tensors = [tf.ragged.constant(strings[i:i+n]) for i in range(0, len(strings), n)]

    # Create ngrams using tf.raw_ops.RaggedNgram
    ngrams = tf.raw_ops.RaggedNgram(ragged_tensors, n)

    return ngrams
