import tensorflow as tf
from tensorflow.raw_ops import EncodeRaggedTensor

# Here is an example of how to use EncodeRaggedTensor
rt_input = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
values = rt_input.values
row_splits = rt_input.row_splits
encoded_rt = EncodeRaggedTensor(values=values, splits=row_splits)
