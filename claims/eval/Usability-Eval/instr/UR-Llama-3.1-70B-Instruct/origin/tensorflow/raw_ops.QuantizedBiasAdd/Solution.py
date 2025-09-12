# Import necessary libraries
import tensorflow as tf

# Define the input tensor and bias
input_tensor = tf.constant([1, 2, 3, 4], dtype=tf.float32)
bias = tf.constant([0.5, 0.5, 0.5, 0.5], dtype=tf.float32)

# Add bias to input tensor for quantized types
quantized_input = tf.raw_ops.QuantizedAdd(input_tensor, 
                                         bias, 
                                         min_input=-128, 
                                         max_input=127, 
                                         min_output=-128, 
                                         max_output=127)

# Alternative way using tf.raw_ops.Add (assuming they are of the same type)
alternative_add = tf.raw_ops.Add(input=input_tensor, 
                                 bias=bias)

# Run a session to see results
sess = tf.Session()
print(quantized_input)
sess.run(alternative_add)
sess.close()
