import tensorflow as tf

def quantize_dequantize_tensor(input_tensor):
    # Quantization
    min_val = tf.reduce_min(input_tensor)
    max_val = tf.reduce_max(input_tensor)
    input_tensor_scaled = (input_tensor - min_val) / (max_val - min_val)
    quantized_tensor = tf.quantization.quantize(input_tensor_scaled, 0, 255, tf.quint8)

    # Dequantization
    dequantized_tensor_scaled = tf.quantization.dequantize(quantized_tensor, 0, 255)
    dequantized_tensor = dequantized_tensor_scaled * (max_val - min_val) + min_val

    return dequantized_tensor
