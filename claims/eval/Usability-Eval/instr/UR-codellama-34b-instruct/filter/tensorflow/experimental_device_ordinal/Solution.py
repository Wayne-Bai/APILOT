
import tensorflow as tf

def get_virtual_device_ordinals(physical_device, location):
    # Get the list of physical devices available on the system
    device_list = tf.config.get_visible_devices()
    
    # Find the index of the physical device in the list
    device_index = device_list.index(physical_device)
    
    # Create a mapping from physical device indices to ordinal numbers
    virtual_device_ordinals = {i: i for i, _ in enumerate(device_list)}
    
    # Return the ordinal number of the specified physical device
    return virtual_device_ordinals[device_index]
