# importing the tensorflow
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint

# set a random seed for reproducibility
tf.random.set_seed(0)

# create a sequential model
model = Sequential()
model.add(Dense(32, input_dim=8, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# checkpoint to save the model after every epoch
cp_callback = ModelCheckpoint('model.h5', save_weights_only=True, verbose=1)

# let's assume we have X_train, X_test, y_train, y_test from sklearn's split_dataset method
# train the model
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, callbacks=[cp_callback], verbose=0)

# evaluate the model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print('Test Accuracy: %.2f' % (accuracy*100))

# predict probabilities for test set
yhat_probs = model.predict(X_test, verbose=0)

# predict crisp classes for test set
yhat_classes = model.predict_classes(X_test, verbose=0)

# evaluate the model
accuracy = metrics.accuracy_score(y_test, yhat_classes)
print('Test Accuracy: %.2f' % (accuracy*100))

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
