import tensorflow as tf

# Define the Mesh Configuration
mesh_config = tf.MeshConfigProto()

# Add the list of Mesh Dimensions
mesh_config.dims = [tf.TensorShapeProto(dim=[tf.TensorShapeProto.Dim(size=10)])]

# Set the device type
mesh_config.device_type = "GPU"

# Set the locality
mesh_config.locality.known_devices = ["/job:localhost/replica:0/task:0/device:GPU:0"]

# Set the task
mesh_config.task.index = 0
mesh_config.task.type = "worker"
