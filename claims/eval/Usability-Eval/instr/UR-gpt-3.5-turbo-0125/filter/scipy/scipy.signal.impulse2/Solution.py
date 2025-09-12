
import numpy as np
import scipy.signal as signal

# Define system coefficients
numerator = [1]
denominator = [1, 2, 1]

# Calculate impulse response
t, h = signal.impulse((numerator, denominator))

print("Impulse response:")
for i in range(len(t)):
    print(f"t = {t[i]}, h = {h[i]}")
