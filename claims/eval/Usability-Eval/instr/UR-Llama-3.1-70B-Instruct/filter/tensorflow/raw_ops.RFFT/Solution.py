import tensorflow as tf

# Function to perform real-valued fast Fourier transform
def real_valued_fft(input_tensor):
    # Use tf.raw_ops.RFFT to perform real-valued fast Fourier transform
    fft = tf.raw_ops.RFFT(input=input_tensor)
    
    # Return the result
    return fft

# Test the function
if __name__ == "__main__":
    # Create a real-valued input tensor
    input_tensor = tf.random.normal(shape=[10, 10])

    # Perform real-valued fast Fourier transform
    result = real_valued_fft(input_tensor)

    # Print the result
    print(result)
