
import tensorflow as tf

def quantize_dequantize_tensor(tensor):
    min_val = tf.reduce_min(tensor)
    max_val = tf.reduce_max(tensor)
    
    quantized_tensor = tf.quantization.quantize(tensor, min_val, max_val, tf.quint8)
    
    dequantized_tensor = tf.quantization.dequantize(quantized_tensor, min_val, max_val)
    
    return dequantized_tensor
