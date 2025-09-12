import numpy as np

try:
    # Create a 1D numpy array
    array = np.array([1, 2, 3])
    
    # Attempt to operate on the array with an invalid axis (axis 1 for a 1D array)
    np.sum(array, axis=1)  # This should raise an AxisError
    
except np.AxisError as e:
    print(f"AxisError caught: {e}")
except ValueError as e:
    print(f"ValueError caught: {e}")
except IndexError as e:
    print(f"IndexError caught: {e}")

# Create a 2D numpy array
array_2d = np.array([[1, 2], [3, 4]])

try:
    # Attempt to operate on the array with an invalid axis (axis 2 for a 2D array)
    np.sum(array_2d, axis=2)  # This should raise an AxisError
    
except np.AxisError as e:
    print(f"AxisError caught: {e}")
except ValueError as e:
    print(f"ValueError caught: {e}")
except IndexError as e:
    print(f"IndexError caught: {e}")
