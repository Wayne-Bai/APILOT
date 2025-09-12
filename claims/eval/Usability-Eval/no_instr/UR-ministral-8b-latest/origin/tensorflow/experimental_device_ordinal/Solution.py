import tensorflow as tf

# Function to get the physical ids and ordinals of devices
def get_device_info():
    physical_devices = tf.config.list_physical_devices()
    for device in physical_devices:
        ordinal = tf.constant(device.ordinal, dtype=tf.int32).numpy()
        physical_id = tf.constant(device.id, dtype=tf.int32).numpy()
        device_name = device.name
        print(f"Device Name: {device_name}, Physical ID: {physical_id}, Ordinal: {ordinal}")

# Get device info
get_device_info()
