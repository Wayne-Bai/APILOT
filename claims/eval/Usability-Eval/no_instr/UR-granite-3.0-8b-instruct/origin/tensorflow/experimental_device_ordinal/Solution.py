import tensorflow as tf

def get_ordinal_device(devices):
    """
    Given a list of devices, return the device with the lowest ordinal number.
    If there are multiple devices with the same ordinal number, return the one with the lowest physical device id.
    """
    devices = sorted(devices, key=lambda x: (x.ordinal, x.physical_device_desc))
    return devices[0]

# Example usage:
devices = tf.config.list_logical_devices('GPU')
ordinal_device = get_ordinal_device(devices)
print(f"The device with the lowest ordinal number is: {ordinal_device.name}")
