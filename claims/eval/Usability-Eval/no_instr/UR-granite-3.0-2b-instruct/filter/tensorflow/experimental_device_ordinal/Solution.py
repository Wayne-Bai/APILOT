import tensorflow as tf

def order_devices():
    device_list = tf.config.list_physical_devices()
    devices = [d.name for d in device_list]
    devices.sort(key=lambda x: (devices.index(x), x))
    return devices

order_devices()
