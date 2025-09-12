import tensorflow as tf

# Disable MLIR-based TensorFlow Compiler Optimizations
tf.config.optimizer.set_jit(False)
