import tensorflow as tf

# Create a multidimensional array (tensor)
array_shape = (3, 4)  # Example shape of the array
multidimensional_array = tf.random.uniform(array_shape, minval=0, maxval=10, dtype=tf.float32)

print("Multidimensional array:")
print(multidimensional_array)
