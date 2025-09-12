import tensorflow as tf

def quantize_dequantize(x, min_val, max_val):
    # Quantize the tensor to quantized data type
    quantized_tensor = tf.quantization.quantize(
        input=x, 
        min_range=min_val, 
        max_range=max_val, 
        T=tf.qint8, 
        mode="MIN_FIRST"
    )[0]  # Retrieve only quantized output, discard min_range and max_range returned

    # Dequantize the tensor back to floating point
    dequantized_tensor = tf.quantization.dequantize(
        input=quantized_tensor, 
        min_range=min_val, 
        max_range=max_val, 
        T=tf.quint8
    )

    return dequantized_tensor

# Example usage
if __name__ == "__main__":
    tensor = tf.constant([1.0, 2.0, 3.0, 4.0])
    min_val = 0.0
    max_val = 4.0
    
    result = quantize_dequantize(tensor, min_val, max_val)
    print(result)
