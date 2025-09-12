import tensorflow as tf

# Disable MLIR-Based TensorFlow Compiler Optimizations
tf.compat.v1.enable_eager_execution()
tf.compat.v1.config.run_functions_eagerly(True)
tf.compat.v1.experimental_compiler.set_mlir_enabled(False)
