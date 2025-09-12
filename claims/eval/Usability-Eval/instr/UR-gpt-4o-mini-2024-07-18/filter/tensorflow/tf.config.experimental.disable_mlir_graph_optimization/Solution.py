import tensorflow as tf

# Disable experimental MLIR-based TensorFlow compiler optimizations
tf.config.optimizer.set_jit(False)

# Your TensorFlow code goes here
