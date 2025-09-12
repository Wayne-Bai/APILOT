import tensorflow as tf

# Assuming you want to create a multi-dimensional tensor of shape (2, 3, 4)
tensor = tf.constant([[i / 3 for i in range(4)] for j in range(3) for _ in range(2)], dtype=tf.float32)
print("Tensor created using numpy-like slicing:\n", tensor)

# Assuming you want to create a dense (fully connected) layer
dense_layer = tf.keras.layers.Dense(units=16, activation='relu')
print("Dense layer created with 16 units and ReLU activation:\n", dense-layer)
