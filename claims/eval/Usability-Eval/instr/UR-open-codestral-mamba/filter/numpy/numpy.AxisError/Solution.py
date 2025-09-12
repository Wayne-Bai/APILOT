import numpy as np

try:
    # Here, we are trying to access a axis that is greater than the number of dimensions of the given numpy array
    arr = np.random.rand(5, 5)
    non_existing_axis = arr[0,:,2,:]

except IndexError:
    # If the error is IndexError, then the issue was with the size of the axis, let's expand the size
    print("Size of the axis was greater than array dimensions, expanding the size...")
    non_existing_axis = arr[..., np.newaxis, :]
    print(f"New shape: {non_existing_axis.shape}")

