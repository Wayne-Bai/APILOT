import tensorflow as tf

# Enable the DTensor namespace
physical_devices = tf.config.list_physical_devices('GPU')
try:
    tf.config.experimental.set_visible_devices(physical_devices, 'GPU')
    tf.config.experimental.dtensor.initialize()
    tf.config.experimental.dtensor.set_tensor_shape_inference(True)
except Exception as e:
    print(e)

# Create a DTensor
dtensor_a = tf.experimental.dtensor.initialize(tf.constant([1.0, 2.0, 3.0, 4.0]))
dtensor_b = tf.experimental.dtensor.initialize(tf.constant([5.0, 6.0, 7.0, 8.0]))

# Perform operations on DTensors
dtensor_c = tf.experimental.dtensor.add(dtensor_a, dtensor_b)

# Print the resulting DTensor
print(dtensor_c)
