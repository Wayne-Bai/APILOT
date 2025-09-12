import tensorflow as tf
""
def create_ngrams(inputs, n):
    '''Creates ngrams from ragged string data.'''
    # Initialize tensors
    output_ids, output_cnt = [], []
    # Process each sequence
    for seq in inputs:
        ids, cnt = [], []
        for i in range(len(seq) - n + 1):
            # Create ngram
            ngram = tf.strings.join(seq[i:i+n], separator=' ')
            ids.append(ngram)
            cnt.append(1)
        # Aggregate ngrams
        output_ids.append(ids)
        output_cnt.append(cnt)
    # Convert lists to tensors
    output_ids = tf.ragged.stack(output_ids, ragged_rank=1)
    output_cnt = tf.ragged.stack(output_cnt, ragged_rank=1)
    return output_ids, output_cnt

# define the input strings
inputs = [
    tf.constant(["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dogs"]),
    tf.constant(["the", "quick", "brown", "dog", "jumps", "quickly", "past", "the", "lazy", "dogs"]),
]

# Test the function with n=3
ngram_ids, ngram_cnt = create_ngrams(inputs, 3)

ngram_ids, ngram_cnt

