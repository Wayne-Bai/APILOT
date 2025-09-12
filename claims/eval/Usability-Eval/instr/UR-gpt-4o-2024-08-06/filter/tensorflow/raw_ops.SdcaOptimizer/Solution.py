import tensorflow as tf

# Define model parameters
W = tf.Variable(tf.random.normal([1]), name='weight')
b = tf.Variable(tf.zeros([1]), name='bias')

# Define a simple linear model
def linear_model(X):
    return W * X + b

# Define the loss function
def loss_fn(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))

# Prepare the input data
X_train = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)
y_train = tf.constant([2.0, 4.0, 6.0, 8.0], dtype=tf.float32)

# Define the optimizer (Stochastic Gradient Descent)
optimizer = tf.optimizers.SGD(learning_rate=0.01)

# Optimization process
@tf.function
def train_step(X, y):
    with tf.GradientTape() as tape:
        predictions = linear_model(X)
        loss = loss_fn(y, predictions)
    gradients = tape.gradient(loss, [W, b])
    optimizer.apply_gradients(zip(gradients, [W, b]))
    return loss

# Training loop
for epoch in range(1000):
    loss_value = train_step(X_train, y_train)
    if epoch % 100 == 0:
        print(f"Epoch {epoch}: Loss: {loss_value.numpy()}")

print("Trained Weights:", W.numpy())
print("Trained Bias:", b.numpy())
