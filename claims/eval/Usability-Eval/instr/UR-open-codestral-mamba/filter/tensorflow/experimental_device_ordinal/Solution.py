import tensorflow as tf

# Check if any GPUs are available
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Get a list of all GPUs
gpus = tf.config.experimental.list_physical_devices('GPU')

# If no GPUs are available, default to a single CPU
if not gpus:
    print("No GPUs available, defaulting to CPU.")
    tf.config.experimental.set_visible_devices([], 'GPU')
else:
    # Order GPUs by their ordinal numbers
    gpus.sort(key=lambda x: x.split('GPU:')[1])

    # Set the order of GPU devices
    tf.config.experimental.set_visible_devices(gpus, 'GPU')
