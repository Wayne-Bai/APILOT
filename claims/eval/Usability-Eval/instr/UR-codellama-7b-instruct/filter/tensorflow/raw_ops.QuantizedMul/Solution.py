
import tensorflow as tf

def quantized_mul(x, y):
    # Quantize inputs
    x = tf.quantization.quantize(x)
    y = tf.quantization.quantize(y)
    
    # Perform element-wise multiplication
    result = x * y
    
    # Dequantize output
    result = tf.quantization.dequantize(result)
    
    return result
