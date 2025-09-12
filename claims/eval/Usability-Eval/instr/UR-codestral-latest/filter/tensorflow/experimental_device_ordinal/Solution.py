import tensorflow as tf

# Get the list of physical GPUs
gpus = tf.config.experimental.list_physical_devices('GPU')

# If there are GPUs, sort them based on ordinal number, device id, and physical location
if gpus:
  gpus.sort(key=lambda gpu: (gpu.name.split(':')[1], gpu.name.split(':')[2]))

# Set memory growth for each GPU
for gpu in gpus:
  tf.config.experimental.set_memory_growth(gpu, True)

# Make the first GPU primary
if gpus:
  tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
