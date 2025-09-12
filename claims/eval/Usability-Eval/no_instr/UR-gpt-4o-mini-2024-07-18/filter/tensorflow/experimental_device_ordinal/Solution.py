import tensorflow as tf

def get_ordered_virtual_devices():
    # Get the list of physical devices
    physical_devices = tf.config.list_physical_devices('GPU')
    
    # Create a list for logical devices
    logical_devices = []
    
    for physical_device in physical_devices:
        # Get the list of logical devices for each physical device
        logical_device_count = tf.config.experimental.get_virtual_device_configuration(physical_device)
        for idx in range(len(logical_device_count)):
            logical_devices.append((physical_device, idx))

    # Sort logical devices based on their ordinal number
    logical_devices_sorted = sorted(logical_devices, key=lambda x: (x[1], physical_devices.index(x[0])))

    # Return sorted logical devices
    return logical_devices_sorted

# Example of usage
ordered_devices = get_ordered_virtual_devices()
for device in ordered_devices:
    print(f"Physical Device: {device[0]}, Logical Device ID: {device[1]}")
