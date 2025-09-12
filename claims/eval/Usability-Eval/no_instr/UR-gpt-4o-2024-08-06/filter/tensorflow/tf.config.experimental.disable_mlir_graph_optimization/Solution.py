import tensorflow as tf

# Disable experimental MLIR-Based TensorFlow Compiler Optimizations
tf.config.optimizer.set_experimental_options({'disable_meta_optimizer': True})

# Example to confirm the setting is applied
a = tf.constant([1.0, 2.0])
b = tf.constant([3.0, 4.0])
c = a + b
print(c)
