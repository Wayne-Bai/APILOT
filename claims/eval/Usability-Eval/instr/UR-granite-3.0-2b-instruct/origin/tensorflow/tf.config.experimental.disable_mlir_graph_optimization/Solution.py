import tensorflow as tf

# Disable experimental MLIR-Based TensorFlow Compiler Optimizations
tf.config.set_optimizer_optimization_level(tf.Optimizer.L0)
