import tensorflow as tf

def quantize_and_dequantize_v4_grad(grad, input, input_min, input_max, axis, num_bits, narrow_range, round_mode):
    with tf.GradientTape() as tape:
        tape.watch(input)
        q = tf.quantization.quantize_and_dequantize_v2(
            input=input,
            input_min=input_min,
            input_max=input_max,
            num_bits=num_bits,
            narrow_range=narrow_range,
            axis=axis,
            round_mode=round_mode
        )
    return tape.gradient(q, input, output_gradients=grad)

# Example usage
input_tensor = tf.constant([1.0, 2.5, 3.0], dtype=tf.float32)
input_min = tf.reduce_min(input_tensor)
input_max = tf.reduce_max(input_tensor)
grad_tensor = tf.constant([0.1, 0.2, 0.3], dtype=tf.float32)

gradient = quantize_and_dequantize_v4_grad(
    grad=grad_tensor,
    input=input_tensor,
    input_min=input_min,
    input_max=input_max,
    axis=-1,
    num_bits=8,
    narrow_range=False,
    round_mode="HALF_TO_EVEN"
)

print("Gradient:", gradient)
