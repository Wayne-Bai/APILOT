import tensorflow as tf
from tensorflow.keras import Model, layers

class MyModel(Model):

  def __init__(self):
    super(MyModel, self).__init__()
    self.d1 = layers.Dense(10, activation='relu')
    self.d2 = layers.Dense(5)

  def call(self, x):
    x = self.d1(x)
    return self.d2(x)

# Create an instance of the model
model = MyModel()

# Let's assume that we have a dataset 'ds'
# ds is a tensorflow.data.Dataset object
ds = ...  # your dataset here

loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.Adam()

checkpoint_path = "training/cp.ckpt"
checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)

@tf.function
def train_step(data, labels):
  with tf.GradientTape() as tape:
    predictions = model(data)
    loss = loss_object(labels, predictions)
  gradients = tape.gradient(loss, model.trainable_variables)
  optimizer.apply_gradients(zip(gradients, model.trainable_variables))

epochs = 5
for epoch in range(epochs):
  for data, labels in ds:
    train_step(data, labels)

  if (epoch + 1) % 5 == 0:
    checkpoint.save(file_prefix=checkpoint_path)
