import tensorflow as tf

# Create a variable with a specific layout
layout = tf.dtensor.Layout(
    shard_specs=[tf.dtensor.ShardSpec(axis=0, num_shards=2)],
    mesh=tf.dtensor.Mesh(names=['x'], devices=["CPU:0", "CPU:1"])
)

# Create a DTensor with the specified layout and some initial data
initial_data = tf.random.uniform((4, 4))
dtensor = tf.dtensor.copy_to_mesh(initial_data, layout)

print("DTensor:", dtensor)
print("Layout of the DTensor:", dtensor.layout)
