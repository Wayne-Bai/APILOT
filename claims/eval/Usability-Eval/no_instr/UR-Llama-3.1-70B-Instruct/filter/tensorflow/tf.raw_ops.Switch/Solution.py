# Import necessary tensorflow modules
import tensorflow as tf

# Define a function to forward data to output ports
def forward_data_to_output_port(pred, input_data):
    # Use tf.raw_ops to create a 'RefSwitch' operation 
    # that forwards data to the output port determined by pred.
    output = tf.raw_ops.RefSwitch(ref=input_data, data=[input_data], predicates=[pred])
    
    return output

# Create a tensor to hold the data
data = tf.Variable(10, dtype=tf.int32)

# Create a tensor to hold the predicate
predicate = tf.constant(True)

# Forward the data to the output port
output_port = forward_data_to_output_port(predicate, data)

# Create a session to execute the 'RefSwitch' operation
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    result = sess.run(output_port)
    
    print(result)
