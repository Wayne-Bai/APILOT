# Importing the necessary library
import tensorflow as tf

# Creating a variable and updating it
def main():
    # Create a variable
    var = tf.Variable(tf.constant([1.0, 2.0, 3.0, 4.0, 5.0]))

    # Divides sparse updates into the variable referenced by resource.
    op = tf.raw_ops.ResourceScatterNdDiv(ref=var.handle, dtype=var.dtype, indices=[[0], [2], [4]], updates=[10.0, 20.0, 30.0])

    # Initialize the variable
    init = tf.global_variables_initializer()

    # Create a session
    with tf.Session() as sess:
        # Run the initializer
        sess.run(init)

        # Run the update operation
        sess.run(op)

        # Print the updated variable
        print(sess.run(var))

if __name__ == "__main__":
    main()
