import numpy as np

# Get the minimum and maximum values of float16, float32, and float64
print("float16: Min = ", np.finfo(np.float16).min, " Max = ", np.finfo(np.float16).max)
print("float32: Min = ", np.finfo(np.float32).min, " Max = ", np.finfo(np.float32).max)
print("float64: Min = ", np.finfo(np.float64).min, " Max = ", np.finfo(np.float64).max)

# Get the smallest and largest positive values of float16, float32, and float64
print("float16: Smallest positive value = ", np.finfo(np.float16).tiny)
print("float32: Smallest positive value = ", np.finfo(np.float32).tiny)
print("float64: Smallest positive value = ", np.finfo(np.float64).tiny)

# Get the largest representable integer of int16, int32, and int64
print("int16: Max = ", np.iinfo(np.int16).max, " Min = ", np.iinfo(np.int16).min)
print("int32: Max = ", np.iinfo(np.int32).max, " Min = ", np.iinfo(np.int32).min)
print("int64: Max = ", np.iinfo(np.int64).max, " Min = ", np.iinfo(np.int64).min)
