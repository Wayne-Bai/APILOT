import numpy as np

print("Machine limits for floating point types:")
print("Lower limit: ", np.finfo(np.float32).min)
print("Upper limit: ", np.finfo(np.float32).max)
print("Machine epsilon: ", np.finfo(np.float32).eps)
