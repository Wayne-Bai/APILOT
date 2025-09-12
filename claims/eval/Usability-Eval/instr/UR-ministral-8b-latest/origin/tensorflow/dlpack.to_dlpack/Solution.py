import tensorflow as tf

# Create a tensor
tensor = tf.constant([1.0, 2.0, 3.0])

# Convert the tensor to a DLpack capsule
dlpack = tf.dlpack.to_tensor(tensor)

print(dlpack)
