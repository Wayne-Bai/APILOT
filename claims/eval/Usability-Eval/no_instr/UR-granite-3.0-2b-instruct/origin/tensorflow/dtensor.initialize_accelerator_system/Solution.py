import tensorflow as tf

# Initializes accelerators and communication fabrics for DTensor
tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(tf.config.list_physical_devices('GPU')[0], True)

# Check if GPU is available
if tf.test.is_built_with_cuda():
    print("GPU is available")
else:
    print("GPU is not available")
