import tensorflow as tf

# Define a simple linear model
class LinearModel(tf.Module):
    def __init__(self):
        self.W = tf.Variable([[0.0]], dtype=tf.float32)
        self.b = tf.Variable([0.0], dtype=tf.float32)

    def __call__(self, x):
        return tf.matmul(x, self.W) + self.b

model = LinearModel()

# Define a loss function
def loss(target_y, predicted_y):
    return tf.reduce_mean(tf.square(target_y - predicted_y))

# Define a training function
def train(model, x, y, lr=0.01):
    with tf.GradientTape() as tape:
        current_loss = loss(y, model(x))
    dW, db = tape.gradient(current_loss, [model.W, model.b])
    model.W.assign_sub(lr * dW)
    model.b.assign_sub(lr * db)

# Dummy data
x_train = tf.constant([[1.0], [2.0], [3.0]], dtype=tf.float32)
y_train = tf.constant([[2.0], [4.0], [6.0]], dtype=tf.float32)

# Training the model with initial data
epochs = 100
for epoch in range(epochs):
    train(model, x_train, y_train)

# New data to continue execution with more feeds and fetches
x_new = tf.constant([[4.0], [5.0]], dtype=tf.float32)
y_new = tf.constant([[8.0], [10.0]], dtype=tf.float32)

# Continue training with new data
for epoch in range(epochs):
    train(model, x_new, y_new)

# Check the model's predictions
print("Predictions on x_new: ", model(x_new).numpy())
