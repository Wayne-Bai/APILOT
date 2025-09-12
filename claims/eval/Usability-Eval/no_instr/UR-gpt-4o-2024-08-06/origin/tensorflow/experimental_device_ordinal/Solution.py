import tensorflow as tf

# List all the physical devices
physical_devices = tf.config.experimental.list_physical_devices('GPU')

# Check if any physical devices are found
if physical_devices:
    # Sort devices based on their physical device id
    physical_devices = sorted(physical_devices, key=lambda x: x.name)
    
    # Set memory growth for each device
    for device in physical_devices:
        tf.config.experimental.set_memory_growth(device, True)
    
    # Create a logical device configuration
    logical_devices_config = [tf.config.LogicalDeviceConfiguration(memory_limit=4096) for _ in physical_devices]
    
    # Apply the logical device configuration
    tf.config.experimental.set_virtual_device_configuration(physical_devices[0], logical_devices_config)
    
    # Verify the logical device configuration
    logical_devices = tf.config.experimental.list_logical_devices('GPU')
    for i, logical_device in enumerate(logical_devices):
        print(f"Logical Device {i}: {logical_device}")

else:
    print("No physical GPU devices found.")
