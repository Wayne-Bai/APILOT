import numpy as np

a = np.array([[1, 2], [3, 4]])
s, ln_det = np.linalg.slogdet(a)

print(f"sign: {s}, log(det): {ln_det}")
