import tensorflow as tf

def initialize_variables():
    # Define the variable initializer
    initializer = tf.initializers.GlorotUniform()

    # Define the variable scope
    with tf.variable_scope("my_scope", initializer=initializer):
        # Create variables under the defined scope
        a = tf.get_variable("a", shape=[2, 3])
        b = tf.get_variable("b", shape=[3, 5])

    # Return variables
    return a, b

# Create TensorFlow session and initialize variables
with tf.Session() as sess:
    a, b = initialize_variables()
    sess.run(tf.global_variables_initializer())
    print("Variable a:\n", sess.run(a))
    print("Variable b:\n", sess.run(b))
