# Import necessary libraries
import tensorflow as tf

# Check if GPU is available
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("GPU is available")
else:
    print("GPU is not available")

# Initialize accelerators
try:
    # Use TPU if available
    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    tf.config.experimental_connect_to_cluster(resolver)
    tf.tpu.experimental.initialize_tpu_system(resolver)
    strategy = tf.distribute.TPUStrategy(resolver)
except ValueError:
    # Otherwise use GPU or CPU
    if gpus:
        strategy = tf.distribute.MirroredStrategy(devices=["/gpu:0"])
    else:
        strategy = tf.distribute.OneDeviceStrategy(device="/cpu:0")

# Create a DTensor device
_mesh = tf.distribute.experimental.CollectiveCommunication.NCCL
device_type = "GPU" if gpus else "CPU"
_mesh = tf.distribute.experimental_mesh.Mesh(device_type=device_type, mesh=_mesh)

device_ids = []
for i in range(len(tf.config.list_logical_devices(device_type))):
    device_ids.append(f"/{device_type.lower()}:{i}")

locals_dict = {}
for i, device_id in enumerate(device_ids):
    locals_dict[f"{device_type.lower()}_{i}"] = device_id

_mesh = tf.distribute.experimental_mesh.Mesh(devices=device_ids, mesh=_mesh)

locals_dict = {}
for i, device_id in enumerate(device_ids):
    locals_dict[f"{device_type.lower()}_{i}"] = device_id

_mesh = tf.distribute.experimental_mesh.Mesh(devices=device_ids, mesh=_mesh)

# Initialize accelerator and communication fabrics
_mesh = tf.distribute.experimental.CollectiveCommunication.NCCL
device_type = "GPU" if gpus else "CPU"

device_ids = []
for i in range(len(tf.config.list_logical_devices(device_type))):
    device_ids.append(f"/{device_type.lower()}:{i}")

mesh_devices = []
for device in device_ids:
    mesh_devices.append(tf.config.list_logical_devices(device_type)[device_ids.index(device)])

_mesh = tf.distribute.experimental_mesh.Mesh(devices=mesh_devices, mesh=_mesh)

device_mesh = _mesh.to_device_mesh(device_ids)

print("DTensor initialized successfully")
print(f"DTensor devices: {device_ids}")
print(f"DTensor mesh: {device_mesh}")
