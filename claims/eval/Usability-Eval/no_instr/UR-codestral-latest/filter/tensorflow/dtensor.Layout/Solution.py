import tensorflow as tf

# Define your DTensor layout
mesh_shape = (4, 4)
num_devices = 4
layout = tf.experimental.dtensor.create_layout("output_dims: mesh[2], major: columns", mesh_shape)

# Create a DTensor
dtensor = tf.experimental.dtensor.from_tensor(tf.random.normal([16, 16]), layout)

print(dtensor)
