
import tensorflow as tf

scalar_value = 42
tensor = tf.fill(dims=[3, 3], value=scalar_value)

print(tensor)
