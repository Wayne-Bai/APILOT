import scipy.signal

# Define the system's transfer function
num = [1]  # Numerator polynomial
den = [1, 2, 1]  # Denominator polynomial
sys = (num, den)

# Compute the impulse response
impulse_response = scipy.signal.impulse(sys)

# Print the impulse response
print(impulse_response)
