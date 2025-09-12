import ctypes

# Load the library
lib = ctypes.CDLL('path/to/your/library.so')

# Define the argument and return types
lib.your_function.argtypes = [ctypes.c_int, ctypes.c_double]
lib.your_function.restype = ctypes.c_double

# Call the function
result = lib.your_function(1, 2.5)

# Print the result
print(result)
