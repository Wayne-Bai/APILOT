
import tensorflow as tf
from tensorflowğında import dtensor

# Create a DTensor
dtensor_0 = dtensor.DTensor()

# Add dimensions to the DTensor
dtensor_0.set_shape([10, 10])
print("DTensor Shape:", dtensor_0.shape)

# Get the layout information of the DTensor
layout = dtensor_0.layout
print("DTensor Layout:", layout)

# Check if the DTensor is contiguously stored in memory
is_contiguous = dtensor_0.is_contiguous
print("Is DTensor Contiguous?", is_contiguous)

# Convert the DTensor to a TensorFlow tensor
tf_tensor = dtensor_0.to_tensor()
print("Tensor Dimensions:", tf_tensor.shape)
