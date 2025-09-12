import tensorflow as tf

# Import the necessary module from tensorflow.experimental.dtensor
from tensorflow.experimental.dtensor import DTensor

# Create a DTensor object
dtensor = DTensor([1, 2, 3], dtype=tf.float32)

# Print the DTensor object
print(dtensor)
