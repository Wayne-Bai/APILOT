import tensorflow as tf

def inverse_real_fft(selected_signal, input_length=10):
    signal_length = tf.shape(selected_signal)[-1] * 2
    selected_signal_complex = tf.cast(tf.complex(selected_signal, tf.zeros_like(selected_signal)), tf.complex64)
    reversed_selected_signal_complex = tf.reverse(selected_signal_complex, [True, False])
    irfft = tf.signal.fft(reversed_selected_signal_complex, fft_length=signal_length)[...,:input_length]
    return tf.reverse(irfft, [True, False])

# Example usage:
selected_signal = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)
print(inverse_real_fft(selected_signal))
