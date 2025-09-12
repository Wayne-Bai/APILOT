import tensorflow as tf

# Example function for performing a real-valued fast Fourier transform
def real_valued_fft(input_tensor):
    # Ensure the input tensor is of type float32
    input_tensor = tf.cast(input_tensor, dtype=tf.float32)
    
    # Compute the fast Fourier transform
    fft_output = tf.signal.rfft(input_tensor)
    
    return fft_output

# Example usage
if __name__ == "__main__":
    # Create a sample input tensor
    sample_input = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)
    
    # Perform the real-valued FFT
    fft_result = real_valued_fft(sample_input)
    
    # Print the result
    print("FFT result:", fft_result.numpy())
