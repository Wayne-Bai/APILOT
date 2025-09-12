import tensorflow as tf

# Create a 1-dimensional FFT object
fft_1d = tf.signal.fft

# Create a 1-dimensional IFFT object
ifft_1d = tf.signal.ifft

# Create a 2-dimensional FFT object
fft_2d = tf.signal.fft2d

# Create a 2-dimensional IFFT object
ifft_2d = tf.signal.ifft2d

# Create a 3-dimensional FFT object
fft_3d = tf.signal.fft3d

# Create a 3-dimensional IFFT object
ifft_3d = tf.signal.ifft3d

# Define the data to be transformed
data = tf.random.uniform(shape=[8, 8], dtype=tf.complex64)

# Perform a 1-dimensional FFT
fft_1d_out = fft_1d(data)
print("1D FFT Output Shape:", fft_1d_out.shape)

# Perform a 1-dimensional IFFT
ifft_1d_out = ifft_1d(fft_1d_out)
print("1D IFFT Output Shape:", ifft_1d_out.shape)

# Perform a 2-dimensional FFT
fft_2d_out = fft_2d(data)
print("2D FFT Output Shape:", fft_2d_out.shape)

# Perform a 2-dimensional IFFT
ifft_2d_out = ifft_2d(fft_2d_out)
print("2D IFFT Output Shape:", ifft_2d_out.shape)

# Perform a 3-dimensional FFT
fft_3d_out = fft_3d(data)
print("3D FFT Output Shape:", fft_3d_out.shape)

# Perform a 3-dimensional IFFT
ifft_3d_out = ifft_3d(fft_3d_out)
print("3D IFFT Output Shape:", ifft_3d_out.shape)
