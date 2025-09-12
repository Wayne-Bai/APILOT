import tensorflow as tf

# Get the list of all available physical devices
physical_devices = tf.config.list_physical_devices('GPU')

if physical_devices:
    # Sort devices based on their physical device ID and location in the list
    sorted_devices = sorted(physical_devices, key=lambda device: (device.name, device.device_type))

    # Set logical device configuration
    for idx, device in enumerate(sorted_devices):
        tf.config.set_logical_device_configuration(
            device,
            [tf.config.LogicalDeviceConfiguration(memory_limit=1024)])  # Here, 1024 MB is set as the memory limit per logical device
        print(f"Assigned logical device ID {idx} to physical device {device}.")
else:
    print("No physical GPU devices found.")
