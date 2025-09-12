import tensorflow as tf
elems = ...  # A tensor
fn = ...  # A Python function, taking a tensor and returning a tensor

result = tf.map_fn(fn, elems)
