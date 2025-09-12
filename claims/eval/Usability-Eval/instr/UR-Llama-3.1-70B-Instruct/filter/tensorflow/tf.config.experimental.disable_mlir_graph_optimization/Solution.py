# Importing the tensorflow module
import tensorflow as tf

# Disabling experimental MLIR-Based TensorFlow Compiler Optimizations
tf.config.experimental.disable_mlir_bridging()

# Verify whether optimizations are disabled or not
print(tf.config.experimental.get_disable_mlir_bridging())
