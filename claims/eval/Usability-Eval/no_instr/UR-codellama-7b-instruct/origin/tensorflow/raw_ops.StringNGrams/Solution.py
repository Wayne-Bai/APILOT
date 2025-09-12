
import tensorflow as tf
from tensorflow import raw_ops

def create_ngrams(input_data, n):
    """
    Creates ngrams from ragged string data.

    Args:
        input_data (RaggedTensor): The input data to generate ngrams from.
        n (int): The number of consecutive characters to combine into an ngram.

    Returns:
        RaggedTensor: A ragged tensor containing the generated ngrams.
    """
    # Convert input_data to a dense tensor if it is not already
    if not isinstance(input_data, tf.RaggedTensor):
        input_data = tf.convert_to_tensor(input_data)

    # Create a sliding window iterator over the input data with a step size of n
    it = raw_ops.SlidingWindow(
        inputs=input_data,
        start=0,
        stop=len(input_data),
        step=n,
        begin_mask=1,
        end_mask=1,
        ellipsis_mask=0,
        new_axis_mask=0,
        shrink_axis_mask=0,
    )

    # Initialize an empty list to store the generated ngrams
    ngrams = []

    for start, stop in it:
        # Get the slice of the input data that corresponds to this window
        slice = input_data[start:stop]

        # Convert the slice to a dense tensor if it is not already
        if not isinstance(slice, tf.Tensor):
            slice = tf.convert_to_tensor(slice)

        # Concatenate the slice with itself shifted by 1 position for each ngram
        for i in range(n):
            ngrams.append(tf.concat([slice[i:], slice[:i]], axis=0))

    # Convert the list of ngram tensors to a ragged tensor and return it
    return tf.ragged.constant(ngrams)
