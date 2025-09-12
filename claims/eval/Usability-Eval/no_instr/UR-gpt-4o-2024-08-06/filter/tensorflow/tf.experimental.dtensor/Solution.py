import tensorflow as tf

def example_dtensor_operation():
    # Create a mesh for the operation
    mesh = tf.experimental.dtensor.create_mesh(['x', 'y'],
                                               [2, 2])

    # Create a dtensor with the desired shape and layout
    dtensor = tf.experimental.dtensor.pack(
        [tf.constant([[1, 2], [3, 4]], dtype=tf.float32), 
         tf.constant([[5, 6], [7, 8]], dtype=tf.float32)],
        layout=tf.experimental.dtensor.Layout(['x', 'y'], mesh)
    )

    print("Original DTensor:")
    print(tf.experimental.dtensor.unpack(dtensor))

    # Perform an example operation, like transposition
    transposed_dtensor = tf.experimental.dtensor.transpose(dtensor)

    print("Transposed DTensor:")
    print(tf.experimental.dtensor.unpack(transposed_dtensor))

example_dtensor_operation()
