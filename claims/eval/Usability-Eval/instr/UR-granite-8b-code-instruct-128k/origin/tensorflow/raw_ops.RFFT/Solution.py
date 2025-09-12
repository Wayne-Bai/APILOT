
import tensorflow as tf

# Real-valued fast Fourier transform.
ft = tf.raw_ops.RFFT(input=[1, 2, 3, 4], Tcomplex=tf.float32)
