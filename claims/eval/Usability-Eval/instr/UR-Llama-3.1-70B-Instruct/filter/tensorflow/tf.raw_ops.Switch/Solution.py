import tensorflow as tf

# Create a new TensorFlow operation
# that forwards data to the output port determined by pred.

# Method in tf.raw_ops: 
# RefSwitch(data, pred, name=None)

def ref_switch_example():
    # Create input data
    data = tf.constant([1.0, 2.0, 3.0, 4.0])
    
    # Create a boolean tensor pred
    pred = tf.constant(True)

    # Create a RefSwitch operation
    output = tf.raw_ops.RefSwitch(data=data, pred=pred)

    # Create a TensorFlow session
    with tf.Session() as sess:
        # Run the RefSwitch operation
        output_val = sess.run(output)

        print("Output:", output_val)

if __name__ == "__main__":
    ref_switch_example()
