# Importing the tensorflow
import tensorflow as tf

# Disable experimental MLIR-Based TensorFlow Compiler Optimizations
tf.config.optimizer.set_experimental_options({'disable_mlir_compiler_optimizations': True})
