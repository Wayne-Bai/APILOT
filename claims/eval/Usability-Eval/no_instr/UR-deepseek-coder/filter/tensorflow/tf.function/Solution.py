import tensorflow as tf

def compile_function_to_graph(input_tensor):
    # Define your computation graph here
    output_tensor = tf.square(input_tensor) + 2 * input_tensor + 1
    return output_tensor

# Create a TensorFlow session
with tf.compat.v1.Session() as sess:
    # Define the input tensor
    input_placeholder = tf.compat.v1.placeholder(tf.float32, shape=[None])
    
    # Compile the function into a callable TensorFlow graph
    output_tensor = compile_function_to_graph(input_placeholder)
    
    # Initialize variables
    sess.run(tf.compat.v1.global_variables_initializer())
    
    # Execute the graph with some input data
    input_data = [1.0, 2.0, 3.0]
    result = sess.run(output_tensor, feed_dict={input_placeholder: input_data})
    
    print("Result:", result)
