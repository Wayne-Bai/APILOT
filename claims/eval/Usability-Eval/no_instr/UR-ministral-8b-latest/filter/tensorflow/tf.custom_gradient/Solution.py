import tensorflow as tf
import numpy as np

class CustomGradientWrapper(tf.keras.callbacks.Callback):
    def __init__(self, gradient_fn):
        super(CustomGradientWrapper, self).__init__()
        self.gradient_fn = gradient_fn

    def compute_grad(self, x, y):
        return self.gradient_fn(x, y)

    def on_batch_end(self, batch, logs=None):
        # Retrieve the current batch's loss and model's intermediate layers
        ids = self.model.los.loss_fn._function._id
        log = tf.convert_to_tensor(ids)

        # Forward pass
        y_pred = self.model(x)
        loss = log[0]

        # Gradient calculation
        gradients = tf.GradientTape().gradient([loss], self.model.trainable_variables)

        for var, grad in zip(self.model.trainable_variables, gradients):
            var.assign_sub(grad * self.compute_grad(x, y))

# Example usage
def custom_gradient_fn(x, y):
    return x * y

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(1)
])

optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)
custom_gradient_callback = CustomGradientWrapper(custom_gradient_fn)

model.compile(optimizer=optimizer, loss='mse')

# Example data
x_train = np.random.rand(100, 4)
y_train = np.random.rand(100, 1)

model.fit(x_train, y_train, epochs=5, callbacks=[custom_gradient_callback])
