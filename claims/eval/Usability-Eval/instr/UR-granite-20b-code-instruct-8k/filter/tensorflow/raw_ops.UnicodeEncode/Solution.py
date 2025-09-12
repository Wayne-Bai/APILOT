import tensorflow as tf

def encode_tensor(tensor):
  return tf.raw_ops.UnicodeEncode(input=tensor, input_encoding='UTF-8', output_encoding='UTF-8')
