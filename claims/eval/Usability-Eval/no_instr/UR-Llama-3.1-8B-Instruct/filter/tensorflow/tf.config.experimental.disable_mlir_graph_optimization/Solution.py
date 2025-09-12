import tensorflow as tf

# Disable experimental MLIR-based TensorFlow compiler optimizations
# (these are not stable and may not work as expected)
options = tf.config.SessionOptions()
options.experimental_enable_mlir_optimization = False

# Set the options as the default for all future sessions
tf.config.set_session_options(options)

# Verify the change
print(tf.config.SessionOptions().experimental_enable_mlir_optimization)
