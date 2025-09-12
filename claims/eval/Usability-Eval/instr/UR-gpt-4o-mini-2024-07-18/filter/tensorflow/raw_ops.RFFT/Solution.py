import tensorflow as tf

def compute_real_fft(signal):
    # Ensure the input is a tensor
    signal_tensor = tf.convert_to_tensor(signal, dtype=tf.float32)
    
    # Compute the Real-valued Fast Fourier Transform
    fft_result = tf.signal.rfft(signal_tensor)
    
    return fft_result

# Example usage
if __name__ == "__main__":
    import numpy as np

    # Create a sample signal
    sample_signal = np.array([0.0, 1.0, 0.0, -1.0], dtype=np.float32)
    
    # Compute the Real FFT
    fft_output = compute_real_fft(sample_signal)
    print("FFT Output:", fft_output.numpy())
