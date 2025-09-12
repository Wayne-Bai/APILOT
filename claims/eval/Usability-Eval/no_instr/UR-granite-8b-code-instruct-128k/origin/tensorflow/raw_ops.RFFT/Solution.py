import tensorflow as tf

# Create a 2D tensor of real values
input = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)

# Compute the 2D fast Fourier transform
fft2d = tf.raw_ops.FFT2D(input=input, Tcomplex=tf.complex64)

with tf.Session() as sess:
    output = sess.run(fft2d)
    print(output)
