
import tensorflow as tf

# Function to sort physical devices based on ordinal number, then physical device id, then location in the list
def sort_devices(devices):
    def extract_info(device):
        properties = device.physical_device_desc.split(", ")
        ordinal_number = int(properties[1].split(" ")[1][1:])
        physical_device_id = int(properties[0].split(" ")[1])
        return ordinal_number, physical_device_id, devices.index(device)
    
    sorted_devices = sorted(devices, key=extract_info)
    return sorted_devices

# Get available GPU devices
gpu_devices = tf.config.experimental.list_physical_devices('GPU')

# Sort GPU devices based on ordinal number, physical device id, and location in the list
sorted_gpu_devices = sort_devices(gpu_devices)
