import tensorflow as tf

def ordinal_device_assignment(devices):
    # Sort devices by ordinal number
    sorted_devices = sorted(devices, key=lambda x: x.ordinal)

    # Assign devices based on ordinal number and physical device id
    assigned_devices = []
    for device in sorted_devices:
        # Break ties by using physical device id and location in the list
        assigned_devices.append(device)

    return assigned_devices

# Example usage
devices = [
    tf.config.LogicalDevice("GPU:0"),
    tf.config.LogicalDevice("GPU:1"),
    tf.config.LogicalDevice("GPU:2"),
]

assigned_devices = ordinal_device_assignment(devices)

# Print assigned devices
for device in assigned_devices:
    print(device)
