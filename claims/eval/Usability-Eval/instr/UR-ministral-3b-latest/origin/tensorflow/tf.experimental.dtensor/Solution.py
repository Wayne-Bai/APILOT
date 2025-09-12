import tensorflow as tf

# Example usage of the tf._api.v2.experimental.dtensor namespace
dtensor1 = tf._api.v2.experimental.dtensor.create([[1, 2, 3], [4, 5, 6]], dtype=tf.int32)
print(dtensor1)

# Perform some operations on the dtensor
dtensor2 = tf._api.v2.experimental.dtensor.reduce_max(dtensor1, axis=1)
print(dtensor2)

# Convert dtensor to np.array for further usage
import numpy as np

dtensor_np = dtensor2.numpy()
print(dtensor_np)
