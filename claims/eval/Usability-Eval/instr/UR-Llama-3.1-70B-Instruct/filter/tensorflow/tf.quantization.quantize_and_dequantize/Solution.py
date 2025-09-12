import tensorflow as tf
import numpy as np

# Create a random tensor
tensor = np.random.uniform(0, 1, size=(1, 10))
t = tf.convert_to_tensor(tensor, dtype=tf.float32)

# Quantize the tensor
quant_t = tf.quantization.fake_quant_with_min_max_vars(t, min=-1.0, max=1.0, num_bits=8, narrow_range=False)

# Dequantize the tensor
dequant_t = tf.quantization.dequantize(
    quant_t,
    min_range=-1.0,
    max_range=1.0,
    mode='MIN_COMBINED',
    narrow_range=False,
    axis=None,
    name=None
)

with tf.Session() as sess:
    t_val, quant_t_val, dequant_t_val = sess.run([t, quant_t, dequant_t])
    
    print("Original Tensor:")
    print(t_val)
    print("Quantized Tensor:")
    print(quant_t_val)
    print("Dequantized Tensor:")
    print(dequant_t_val)
