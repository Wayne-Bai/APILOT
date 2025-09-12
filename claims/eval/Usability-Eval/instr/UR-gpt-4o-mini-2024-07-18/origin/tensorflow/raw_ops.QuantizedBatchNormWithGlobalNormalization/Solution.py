import tensorflow as tf

def quantized_batch_norm(input_tensor, scale, offset, mean, variance, variance_epsilon=1e-5):
    # Ensure the input tensor is in the correct shape and type
    input_tensor = tf.convert_to_tensor(input_tensor, dtype=tf.quint8)
    
    # Quantized batch normalization
    output_tensor = tf.raw_ops.QuantizedBatchNorm(
        input=input_tensor,
        scale=scale,
        offset=offset,
        mean=mean,
        variance=variance,
        variance_epsilon=variance_epsilon
    )
    
    return output_tensor
