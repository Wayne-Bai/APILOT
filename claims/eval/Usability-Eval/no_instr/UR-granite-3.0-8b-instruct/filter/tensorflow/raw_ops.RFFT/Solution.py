import tensorflow as tp

# Define a tensor to perform the FFT on
input_tensor = tp.constant([1.0, 2.0, 3.0, 4.0])

# Perform the real-valued fast Fourier transform
fft_result = tp.raw_ops.fft_real(input_tensor)

# Print the result
print(fft_result)
