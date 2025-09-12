
import tensorflow as tf

a = tf.random.normal(shape=(2, 3))
print("Original tensor:")
print(a)

# Transpose the tensor
transposed_a = tf.transpose(a, perm=[1, 0])
print("\nTransposed tensor:")
print(transposed_a)
