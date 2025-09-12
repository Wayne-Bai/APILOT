import tensorflow as tf

# Define a function to perform a real-valued fast Fourier transform
def real_valued_fft(signal):
    # Compute the real-valued FFT
    fft_result = tf.signal.rfft(signal)
    return fft_result

# Example usage
if __name__ == "__main__":
    # Create a sample input signal (1D array)
    sample_signal = tf.constant([0.0, 1.0, 0.0, -1.0], dtype=tf.float32)
    
    # Compute the FFT
    result = real_valued_fft(sample_signal)
    
    # Print the result
    print("FFT Result:", result.numpy())
