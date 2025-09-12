import tensorflow as tf

def quantize_and_dequantize_v4_grad(grad, input, input_min, input_max, axis, mode='MIN_COMBINED', 
                                    round_mode='HALF_TO_EVEN', narrow_range=False, axis_on_output=True):
    # The gradient function for QuantizeAndDequantizeV4 is not directly available, so it's typically custom-defined.
    # Below is a simplified approach that should be refined based on specific requirements and usage context.
    
    with tf.GradientTape() as tape:
        tape.watch(input)
        tape.watch(input_min)
        tape.watch(input_max)
        quantized = tf.quantization.fake_quant_with_min_max_vars(
            input, min=input_min, max=input_max, num_bits=8, narrow_range=narrow_range
        )
        
    # Compute gradients
    gradients = tape.gradient(quantized, [input, input_min, input_max], output_gradients=grad)
    
    # Depending on further need, process these gradients
    return gradients

# Example usage:

# sample input and gradients
input_tensor = tf.constant([1.0, 2.5, 3.75, 4.0], dtype=tf.float32)
input_min = tf.reduce_min(input_tensor)
input_max = tf.reduce_max(input_tensor)
output_grad = tf.constant([0.1, 0.2, 0.3, 0.4], dtype=tf.float32)

# Calculate gradients
gradients = quantize_and_dequantize_v4_grad(output_grad, input_tensor, input_min, input_max, axis=0)

print("Gradients:")
print("dInput:", gradients[0])
print("dInput_min:", gradients[1])
print("dInput_max:", gradients[2])
