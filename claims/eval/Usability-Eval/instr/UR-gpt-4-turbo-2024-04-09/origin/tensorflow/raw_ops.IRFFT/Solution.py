import tensorflow as tf

def inverse_real_fft(input_tensor):
    # Use 'irfft' to perform an Inverse Real-valued Fast Fourier Transform.
    invers_fft = tf.signal.irfft(input_tensor)
    return invers_fft

# Example usage
# Create a complex tensor assumed to be an output from a RFFT operation
fft_tensor = tf.signal.rfft([1.0, 2.0, 3.0, 4.0])

# Compute the inverse real FFT
result = inverse_real_fft(fft_tensor)
print(result)
