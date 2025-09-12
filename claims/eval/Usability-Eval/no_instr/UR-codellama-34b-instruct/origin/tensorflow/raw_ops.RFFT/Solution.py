import tensorflow as tf

# Load audio data into a tensor
audio_data = ...

# Apply a window function to the audio data
window_size = 2048
hann_window = tf.signal.windows.hann(window_size)
audio_data_windowed = audio_data * hann_window[None, :]

# Compute the Fourier transform of the windowed audio data
freq_spectrum = tf.signal.rfft(audio_data_windowed)
