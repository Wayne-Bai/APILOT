import tensorflow as tf

# Define the shape of the DTensor
shape = (2, 3, 4)

# Create a DTensor with the given shape
dtensor = tf. tensors.DTensor(shape)

# Print the layout information of the DTensor
print("Layout information of the DTensor:")
print(dtensor.layout)
