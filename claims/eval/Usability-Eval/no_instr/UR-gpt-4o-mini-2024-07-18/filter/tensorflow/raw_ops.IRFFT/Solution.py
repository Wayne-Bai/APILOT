import tensorflow as tf

# Function to perform Inverse real-valued fast Fourier transform
def inverse_real_fft(x, fft_length=None):
    # Using tf.signal.inverse_real_fft for inverse FFT
    return tf.signal.inverse_real_fft(x, fft_length=fft_length)

# Example usage
if __name__ == "__main__":
    # Sample input: a real-valued 1D array
    x = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)
    
    # Perform inverse real-valued FFT
    output = inverse_real_fft(x)
    print(output.numpy())
