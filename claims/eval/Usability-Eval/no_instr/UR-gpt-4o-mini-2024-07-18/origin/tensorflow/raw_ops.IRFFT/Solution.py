import tensorflow as tf

# Function to perform Inverse FFT using TensorFlow
def inverse_fft(input_tensor):
    # Ensure the input tensor is complex
    if tf.is_tensor(input_tensor):
        input_tensor = tf.cast(input_tensor, tf.complex64)
    else:
        raise TypeError("Input must be a tensor.")

    # Perform the Inverse FFT
    output_tensor = tf.signal.ifft(input_tensor)

    return output_tensor

# Example usage
input_data = tf.constant([1.0, 2.0, 3.0, 4.0])
fft_result = tf.signal.fft(tf.cast(input_data, tf.complex64))
inverse_result = inverse_fft(fft_result)

print("Original Data: ", input_data.numpy())
print("FFT Result: ", fft_result.numpy())
print("Inverse FFT Result: ", inverse_result.numpy())
