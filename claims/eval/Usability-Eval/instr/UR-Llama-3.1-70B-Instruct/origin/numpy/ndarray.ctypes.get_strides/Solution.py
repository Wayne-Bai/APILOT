import ctypes
import numpy as np

# Create a 3D numpy array
array_3d = np.arange(24).reshape(2, 3, 4)

# Get the strides information
strides_info = array_3d.strides

# Convert the strides information into a ctypes array of c_intp
strides_array = (ctypes.c_intp * array_3d.ndim)(*strides_info)

# Print the strides information
print("strides_info:", strides_info)
print("strides_array:", strides_array)
print("strides_array type:", type(strides_array))
for i, stride in enumerate(strides_array):
    print(f"Stride for dimension {i}: {stride} bytes")
