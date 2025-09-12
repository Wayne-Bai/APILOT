import numpy as np

# Machine limits for floating point types
print("Smallest positive number: ", np.finfo(np.float64).eps)
print("Smallest positive number: ", np.finfo(np.float32).eps)
print("Maximum integer number: ", np.iinfo(np.int8).max)
print("Minimum integer number: ", np.iinfo(np.int8).min)
print("Precision: ", np.finfo(np.float64).precision)
print("Exponent range: ", np.finfo(np.float64).iexp)
print("Underflow limit: ", np.finfo(np.float64).tiny)
