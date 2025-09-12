import tensorflow as tf

# Disable experimental MLIR-Based TensorFlow Compiler Optimizations
tf.config.optimizer.set_experimental_options(mlir_compiler_enabled=False)
