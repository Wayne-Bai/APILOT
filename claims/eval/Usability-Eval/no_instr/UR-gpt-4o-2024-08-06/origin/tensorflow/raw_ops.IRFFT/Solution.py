import tensorflow as tf

# Define a complex input tensor
input_data = tf.complex(
    real=[0.0, 1.0, 2.0, 3.0],
    imag=[0.0, 1.0, 1.0, 0.0]
)

# Use tf.signal.ifft for real-valued inverse FFT
# Calculate the inverse FFT
inverse_fft = tf.signal.ifft(input_data)

# Real-valued output typically requires taking the real part
# because the input was real and assumed conjugate symmetric
real_inverse_fft = tf.math.real(inverse_fft)

# Execute the computation
print("Inverse FFT (real part):", real_inverse_fft.numpy())
