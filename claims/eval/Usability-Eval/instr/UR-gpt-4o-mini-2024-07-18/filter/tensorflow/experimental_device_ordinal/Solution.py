import tensorflow as tf

def get_device_ordering():
    gpus = tf.config.experimental.list_physical_devices('GPU')
    
    # Create a list of devices with their respective ordinal numbers and ids
    device_info = []
    for idx, gpu in enumerate(gpus):
        device_info.append((idx, gpu))

    # Sort devices first by ordinal number (idx) and then by physical device_id
    device_info.sort(key=lambda x: (x[0], x[1].device_id))

    # Create a mapping of logical device IDs based on the sorted order
    logical_device_mapping = {info[1].name: i for i, info in enumerate(device_info)}
    
    return logical_device_mapping

# Get the mapping of logical devices according to their ordering
device_ordering = get_device_ordering()
print(device_ordering)
