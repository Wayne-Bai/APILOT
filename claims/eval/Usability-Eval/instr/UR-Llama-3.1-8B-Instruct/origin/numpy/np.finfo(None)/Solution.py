import numpy as np

# check the maximum and minimum values for float32 type
print("float32 Max:", np.finfo(np.float32).max)
print("float32 Min:", np.finfo(np.float32).min)

# check the maximum and minimum values for float64 type
print("float64 Max:", np.finfo(np.float64).max)
print("float64 Min:", np.finfo(np.float64).min)

# check the maximum and minimum values for complex64 type
# These fields are the values that the input types has, maximum and minimum
print("complex64 Max Real Part:", np.finfo(np.complex64).max)
print("complex64 Max Imaginary Part:", np.finfo(np.complex64).max)
print("complex64 Min Real Part:", np.finfo(np.complex64).min)
print("complex64 Min Imaginary Part:", np.finfo(np.complex64).min)

# check the maximum and minimum values for complex128 type
print("complex128 Max Real Part:", np.finfo(np.complex128).max)
print("complex128 Max Imaginary Part:", np.finfo(np.complex128).max)
print("complex128 Min Real Part:", np.finfo(np.complex128).min)
print("complex128 Min Imaginary Part:", np.finfo(np.complex128).min)
