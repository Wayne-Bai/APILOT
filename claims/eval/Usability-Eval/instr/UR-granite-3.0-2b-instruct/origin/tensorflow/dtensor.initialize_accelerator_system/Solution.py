import tensorflow as tf

# Initialize accelerators and communication fabrics for DTensor
physical_devices = tf.config.list_physical_devices()
tf.config.set_visible_devices(physical_devices[0], 'GPU')

# Create a distributed strategy
strategy = tf.distribute.OneDeviceStrategy(physical_devices[0])

# Print the current strategy
print("Number of devices: ", len(physical_devices))
print("Strategy: ", strategy)
