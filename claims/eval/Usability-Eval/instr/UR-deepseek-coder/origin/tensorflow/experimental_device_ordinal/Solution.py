import tensorflow as tf

def order_devices_by_ordinal(physical_devices):
    # Sort the physical devices based on the ordinal number
    sorted_devices = sorted(physical_devices, key=lambda dev: (dev.name, dev.device_type, dev.memory_limit))
    
    # Assign device IDs based on the sorted order
    for idx, device in enumerate(sorted_devices):
        device._device_id = idx
    
    return sorted_devices

# Example usage
physical_devices = tf.config.list_physical_devices('GPU')
ordered_devices = order_devices_by_ordinal(physical_devices)

# Print the ordered devices with their assigned IDs
for device in ordered_devices:
    print(f"Device ID: {device._device_id}, Name: {device.name}, Type: {device.device_type}")
