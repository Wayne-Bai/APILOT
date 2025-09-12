import tensorflow as tf

# Create a tensor of real values
x = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Real-number FFT using tf.raw_ops
fft_result = tf.raw_ops.RealValuedFFT(x, -1)

print("Input Tensor:")
print(x.numpy())

print("FFT Result:")
print(fft_result.numpy())
