import tensorflow as tf

class TFAutoRegressor(tf.keras.Model):
    def __init__(self, num_classes, **kwargs):
        super(TFAutoRegressor, self).__init__(**kwargs)
        self.num_classes = num_classes
        self.dense = tf.keras.layers.Dense(num_classes, activation='softmax')

    def call(self, inputs):
        return self.dense(inputs)

    def fit(self, X, y, batch_size=32, epochs=10):
        self.compile(optimizer=tf.keras.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        self.fit(X, y, batch_size=batch_size, epochs=epochs, verbose=1)

    def predict_proba(self, X):
        return self.dense(X).numpy()

    def predict(self, X):
        return tf.argmax(self.dense(X), axis=-1).numpy()
