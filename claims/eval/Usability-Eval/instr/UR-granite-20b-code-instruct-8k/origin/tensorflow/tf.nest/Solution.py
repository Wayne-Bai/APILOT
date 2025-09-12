import tensorflow as tf

tf.nest.map_structure(fn=lambda x: x + 1, structure=[1, 2, 3])
