
import tensorflow as tf

devices = tf.config.list_physical_devices('GPU')
devices.sort(key=lambda x: (x.ordinal, x.name, x.device_name))

# Assigning logical device ids
for i, device in enumerate(devices):
    tf.config.set_logical_device_configuration(
        device,
        [tf.config.LogicalDeviceConfiguration(memory_limit=0.5)]
    )
