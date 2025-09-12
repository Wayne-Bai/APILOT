import tensorflow as tf

# Assuming you have a tensor 'tensor'

# Gather slices from the tensor at indices
indices = [0, 2, 5]
gather_slices = tf.raw_ops.gather_slices(tensor, indices)

print(gather_slices)
