import tensorflow as tf

# Define the array of flat indices
flat_indices = [1, 2, 3, 4, 5]

# Convert the array of flat indices into a tuple of coordinate arrays
coords = tf.cast(tf.constant(flat_indices), tf.int64)
x = coords % 3
y = (coords // 3) % 2
z = coords // 6

# Print the resulting coordinate arrays
print("x:", x.numpy())
print("y:", y.numpy())
print("z:", z.numpy())
