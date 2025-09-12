import tensorflow as tf

# Initialize accelerators and communication fabrics for DTensor
accelerators = tf.config.experimental.list_physical_devices('GPU')
if len(accelerators) > 0:
    try:
        tf.config.experimental.set_memory_growth(accelerators[0], True)
    except RuntimeError as e:
        #-print('Error: %s %s' % (type(e).__name__, str(e)))
        pass

# Print to verify acceleration configuration
for gpu in tf.config.experimental.list_physical_devices('GPU'):
    print(f"GPU device name: {gpu.name}, device count: {len(tf.config.list_physical_devices('GPU'))}")

