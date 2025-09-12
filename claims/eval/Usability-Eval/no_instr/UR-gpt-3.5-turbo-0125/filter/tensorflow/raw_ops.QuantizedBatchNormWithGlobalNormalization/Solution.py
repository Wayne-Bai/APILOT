
import tensorflow as tf

def quantized_batch_norm(inputs, scale, offset, mean, variance, epsilon, mode,
                           ema_decay, num_bits=8, name=None):
    output, _, _ = tf.raw_ops.QuantizedBatchNorm(
        x=inputs,
        scales=scale,
        offsets=offset,
        population_variance=variance,
        population_mean=mean,
        epsilon=epsilon,
        decay=ema_decay,
        is_training=(mode=='training'),
        num_bits=num_bits,
        name=name
    )
    return output
