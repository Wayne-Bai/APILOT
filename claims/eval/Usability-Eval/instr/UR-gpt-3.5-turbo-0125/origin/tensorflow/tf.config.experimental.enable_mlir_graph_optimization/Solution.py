
import tensorflow as tf

# Enable experimental MLIR-Based TensorFlow Compiler Optimizations
tf.config.optimizer.set_experimental_options({'custom_optimization_config': 'mlir'})
