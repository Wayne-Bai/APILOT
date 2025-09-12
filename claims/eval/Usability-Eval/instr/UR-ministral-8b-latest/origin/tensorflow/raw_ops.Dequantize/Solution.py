import tensorflow as tf

def dequantize_input(input_tensor, input_dtype):
    if input_dtype == tf.bool:
        return tf.cast(input_tensor, tf.float32)

    elif input_dtype in [tf.uint8, tf.int8, tf.uint16, tf.int16]:
        return tf.cast(input_tensor, tf.float32)

    elif input_dtype in [tf.quint8, tf.quint16]:
        return tf.raw_ops.QuantizeV1(input=input_tensor, epsilon=0.0)

    else:
        raise ValueError(f"Unsupported input_dtype: {input_dtype}")

# Example usage:
input_tensor = tf.constant([1, 2, 3, 4], dtype=tf.uint8)
result = dequantize_input(input_tensor, tf.uint8)
print(result)
