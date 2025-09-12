import tensorflow as tf

# Define the matrix size
matrix_size = 10

# Create a random complex matrix
mat = tf.complex(tf.random.uniform([matrix_size, matrix_size]), tf.random.uniform([matrix_size, matrix_size]))

# Compute the 2D Fast Fourier Transform
fft_mat = tf.signal.fft2d(mat)

# Shift the zero-frequency component to the center of the spectrum
fft_shifted = tf.signal.fftshift(fft_mat)
