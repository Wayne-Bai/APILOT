import tensorflow as tf

def get_ordinal_device(devices):
    """
    Given a list of devices, return the device with the lowest ordinal number.
    If there are multiple devices with the same ordinal number, return the one with the lowest physical device id.
    """
    # Sort the devices by ordinal number
    devices.sort(key=lambda x: x.ordinal)

    # If there are multiple devices with the same ordinal number, sort them by physical device id
    devices.sort(key=lambda x: x.physical_device_id)

    return devices[0]

# Get the list of available devices
devices = tf.config.list_logical_devices('GPU')

# Get the device with the lowest ordinal number
ordinal_device = get_ordinal_device(devices)

print(f"The device with the lowest ordinal number is: {ordinal_device.name}")
