import tensorflow as tf

def convert_to_string(tensor):
  return tf.map_fn(lambda x: tf.as_string(x), tensor)
