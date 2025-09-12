
import tensorflow as tf

# Create a sample tensor
tensor = tf.random.normal((3, 4), mean=0.5, stddev=1.0)

# Convert the tensor to a DLPack capsule
dlpack_capsule = tensor._tf_dlpack()

print("DLPack capsule:", dlpack_capsule)
