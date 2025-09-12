import tensorflow as tf

# Creating a DTensor
dt = tf.DTensor(shape=(2, 3), dtype=tf.float32, values=[]
                 )
print(dt)

# Accessing layout information
print(dt.shape)
print(dt.dtype)
print(dt.elements.dtype)
print(dt.elements.shape)

# Additional operations can be performed based on tensor layout
print(dt.values)
