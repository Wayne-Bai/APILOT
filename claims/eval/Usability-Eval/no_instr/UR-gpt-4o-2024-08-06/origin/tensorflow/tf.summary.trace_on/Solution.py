import tensorflow as tf

# Set the logging level
tf.get_logger().setLevel('INFO')

# Start a trace to record computation graphs and profiling information.
def perform_trace():
    with tf.profiler.experimental.Profile('/tmp/my_logdir'):
        # Example of a simple model for which we want to trace computations
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(10, activation='relu', input_shape=(28, 28)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(10)
        ])

        # Dummy data
        x = tf.random.normal((1, 28, 28))
        y = model(x)  # Forward pass

        # Optionally, define loss and optimizer if you want to trace training
        loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
        optimizer = tf.keras.optimizers.Adam()

        # Using tf.GradientTape for capturing the grads
        with tf.GradientTape() as tape:
            predictions = model(x)
            loss = loss_object(tf.constant([1]), predictions)
        
        grads = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(grads, model.trainable_variables))

# Enable TensorFlow profiler
tf.profiler.experimental.start('/tmp/my_logdir')

# Run the trace
perform_trace()

# Stop the profiler
tf.profiler.experimental.stop()
