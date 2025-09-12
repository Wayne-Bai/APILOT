import tensorflow as tf

def quantize_and_dequantize_tensor(tensor, quant_min, quant_max):
    # Quantize the tensor
    quantized = tf.quantization.quantize_and_dequantize(tensor, quant_min, quant_max, name='quantize_and_dequantize')

    return quantized
