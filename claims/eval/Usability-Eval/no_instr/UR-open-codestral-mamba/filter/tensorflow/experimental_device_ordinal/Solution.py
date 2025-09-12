import tensorflow as tf

# Check if TensorFlow can detect Nvidia GPUs
if not tf.test.is_gpu_available(cuda_only=False):
    print("No Nvidia GPUs detected. Exiting.")
    exit()

# Get a list of all logical devices
logical_devices = tf.config.list_logical_devices('GPU')

# Sort the devices by name
sorted_devices = sorted(logical_devices, key=lambda d: d.name)

# Assign ordinal numbers to the devices
for i, device in enumerate(sorted_devices):
    tf.config.experimental.set_virtual_device_configuration(
        device,
        [tf.config.experimental.VirtualDeviceConfiguration(ordinal=i)])
