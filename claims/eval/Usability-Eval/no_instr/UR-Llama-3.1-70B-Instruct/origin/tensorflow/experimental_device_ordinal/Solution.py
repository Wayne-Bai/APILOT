# Import necessary libraries
import tensorflow as tf

# Function to get the list of all visible devices
def get_visible_devices():
    return tf.config.get_visible_devices()

# Function to get the list of all physical devices
def get_physical_devices():
    return tf.config.get_physical_devices('GPU')

# Function to order the devices based on their ordinal number
def order_devices(devices):
    ordered_devices = sorted(devices, key=lambda device: (device.logical_device_id, device.physical_device_id))
    return ordered_devices

# Get the list of visible devices
visible_devices = get_visible_devices()

# Get the list of physical devices
physical_devices = get_physical_devices()

# Order the devices
if physical_devices:
    ordered_devices = order_devices(physical_devices)
    for i, device in enumerate(ordered_devices):
        print(f"Device ID: {i}, Device Name: {device.name}")
else:
    print("No physical devices found.")
