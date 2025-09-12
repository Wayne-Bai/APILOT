import tensorflow as tf

def inverse_real_fast_fft(input_tensor):
    return tf.raw_ops.IFT(input=input_tensor)

# Example usage
if __name__ == "__main__":
    input_data = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.dtypes.complex64)
    output_data = inverse_real_fast_fft(input_data)
    print(output_data)
