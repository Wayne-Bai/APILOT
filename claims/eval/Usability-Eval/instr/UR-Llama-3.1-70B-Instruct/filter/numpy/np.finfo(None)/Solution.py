import numpy as np

# Machine limits for floating point types

def machine_limits():
    # Floating-point type limits
    print("Single precision floating point: ")
    print("Minimum positive value: ", np.finfo(np.float32).min)
    print("Maximum value: ", np.finfo(np.float32).max)
    print("Smallest positive normal value: ", np.finfo(np.float32).eps)

    print("\nDouble precision floating point: ")
    print("Minimum positive value: ", np.finfo(np.float64).min)
    print("Maximum value: ", np.finfo(np.float64).max)
    print("Smallest positive normal value: ", np.finfo(np.float64).eps)

    print("\nLong double precision floating point: ")
    print("Minimum positive value: ", np.finfo(np.longdouble).min)
    print("Maximum value: ", np.finfo(np.longdouble).max)
    print("Smallest positive normal value: ", np.finfo(np.longdouble).eps)

    # Integer type limits
    print("\nSigned integer type limits: ")
    print("Minimum 8-bit signed integer value: ", np.iinfo(np.int8).min)
    print("Maximum 8-bit signed integer value: ", np.iinfo(np.int8).max)
    
    print("\nUnsigned integer type limits: ")
    print("Minimum 8-bit unsigned integer value: ", np.iinfo(np.uint8).min)
    print("Maximum 8-bit unsigned integer value: ", np.iinfo(np.uint8).max)

machine_limits()
