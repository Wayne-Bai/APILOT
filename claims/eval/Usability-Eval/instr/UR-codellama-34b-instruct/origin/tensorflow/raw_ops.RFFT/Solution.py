import tensorflow as tf

# Define the input tensor
input_tensor = tf.random.normal([10, 256], dtype=tf.float32)

# Perform RFFT using tf.raw_ops.RealFft
output_tensor = tf.raw_ops.RealFft(input=input_tensor,
                                   fft_length=256,
                                   batch_dims=[10],
                                   axis=-1)
