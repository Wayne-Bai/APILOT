import tensorflow as tf

# Disables experimental MLIR-Based TensorFlow Compiler Optimizations
tf.config.optimizer.set_jit(enabled=False)
