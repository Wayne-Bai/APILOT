
import tensorflow as tf

mesh_dimensions = [100, 200, 300]
mesh_config = tf.meshgrid(*[tf.range(dim) for dim in mesh_dimensions])

print(mesh_config)
