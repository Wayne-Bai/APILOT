import tensorflow as tf

# Get a list of all available devices
devices = tf.config.list_logical_devices()

# Sort the devices by their ordinal number
sorted_devices = sorted(devices, key=lambda x: x.device_id)

# Print the sorted list of devices
for device in sorted_devices:
    print(device.name)
