import tensorflow as tf
from tensorflow._api.v2.experimental.dtensor import DTensor

# Create a DTensor
dtensor = DTensor(data=tf.constant([1.0, 2.0, 3.0]))

# Print the DTensor
print(dtensor)
