import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')
if gpus:
    # Create a list of GPU devices with their ordinal number, physical device id, and location
    devices_info = []
    for gpu in gpus:
        devices_info.append((gpu.name, gpu.physical_device_desc, gpu.device_id))

    # Sort the list based on the ordinal number, physical device id, and location
    devices_info.sort(key = lambda x: (int(x[0].split(':')[1]), x[2], devices_info.index(x)))

    # Assign device ids based on the sorted order
    for index, device_info in enumerate(devices_info):
        tf.config.set_visible_devices(device_info[0], 'GPU')
        tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)
        tf.config.set_logical_device_configuration(
            device_info[0],
            [tf.config.LogicalDeviceConfiguration(device_id=index)])
