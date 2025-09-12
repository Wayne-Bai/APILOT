import tensorflow as tf

def greedy_decoder(inputs):
  """
  Performs greedy decoding on the logits given in inputs.

  Args:
    inputs: Logits to decode. Should have shape `[batch_size, None, num_classes]`.

  Returns:
    A `Tensor` of shape `[batch_size, None]` containing the decoded predictions.
  """
  predicted_ids = tf.argmax(inputs, axis=-1)
  return predicted_ids
