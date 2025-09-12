import tensorflow as tf

# Set the number of devices you will use and initiate strategy
physical_devices = tf.config.experimental.list_physical_devices('GPU')
for device in physical_devices:
    tf.config.experimental.set_memory_growth(device, True)

logical_devices = tf.config.list_logical_devices('GPU')
print(f"Number of physical GPUs: {len(physical_devices)}")
print(f"Number of logical GPUs: {len(logical_devices)}")

# Instantiate a MultiWorkerMirroredStrategy to initialize accelerators and communication fabrics
strategy = tf.distribute.MultiWorkerMirroredStrategy()

print("DTensor environment initialized successfully with strategy:", strategy)
