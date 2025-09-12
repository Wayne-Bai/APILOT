import tensorflow as tf

# Check the available devices
devices = tf.config.experimental.list_physical_devices()

# Print the devices
for device in devices:
    print(f'Device: {device}, Type: {device.device_type}, Memory: {tf.config.experimental.get_memory_info(device)}')

# Set device to GPU if available, otherwise CPU
for device in devices:
    if device.device_type == 'GPU':
        tf.config.experimental.set_visible_devices(device, 'GPU')
        tf.config.experimental.enable_tensor_float_32_execution(False)

# Print the devices after configuration
devices = tf.config.experimental.list_physical_devices()
for device in devices:
    print(f'Device: {device}, Type: {device.device_type}, Memory: {tf.config.experimental.get_memory_info(device)}')
