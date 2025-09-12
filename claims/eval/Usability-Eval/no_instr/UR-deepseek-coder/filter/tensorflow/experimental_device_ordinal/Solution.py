import tensorflow as tf

def order_devices_by_ordinal(physical_devices):
    # Sort the physical devices based on ordinal number, physical device id, and location in the list
    sorted_devices = sorted(physical_devices, key=lambda dev: (dev.name, dev.device_type, dev.device_index))
    
    # Assign device IDs based on the sorted order
    for idx, device in enumerate(sorted_devices):
        device.device_id = idx
    
    return sorted_devices

# Example usage
physical_devices = tf.config.list_physical_devices('GPU')
ordered_devices = order_devices_by_ordinal(physical_devices)

# Print the ordered devices with their assigned device IDs
for device in ordered_devices:
    print(f"Device ID: {device.device_id}, Name: {device.name}, Type: {device.device_type}, Index: {device.device_index}")
