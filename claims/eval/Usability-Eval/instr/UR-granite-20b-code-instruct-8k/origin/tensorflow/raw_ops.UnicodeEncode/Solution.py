import tensorflow as tf

def encode_tensor(tensor):
  """
  Encodes a tensor of ints into unicode strings.
  Args:
    tensor: A tensor of type int32 or int64.
  Returns:
    A tensor of type string.
  """
  return tf.raw_ops.UnicodeEncode(input=tensor, input_encoding='UTF-8', errors='ignore')
