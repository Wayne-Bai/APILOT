
import tensorflow as tf
from tensorflow.python.client import device_lib

def get_ordinal_number(device):
    # Get the physical device id and location in the list
    physical_device_id = device.physical_device_desc
    location_in_list = device_lib.list_local_devices().index(device)
    
    # Return the ordinal number based on the logical device with lower ordinal number receiving a lower device id
    return min(device.ordinal, location_in_list)
