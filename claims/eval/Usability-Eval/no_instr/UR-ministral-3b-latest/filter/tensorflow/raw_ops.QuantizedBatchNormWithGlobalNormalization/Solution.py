import tensorflow as tf
from tensorflow.keras.layers import Layer, Dense
from tensorflow.keras.quantization import QuantizationScope, Quantize

class QuantizedBatchNormalization(Layer):
    def __init__(self, **kwargs):
        super(QuantizedBatchNormalization, self).__init__(**kwargs)
        self.saved_inputs = []
        self._quantization_config = QuantizationScope.display_config()

    def build(self, input_shape):
        super(QuantizedBatchNormalization, self).build(input_shape)
        self.kernel = self.add_weight(
            shape=(1,),
            initializer='zero',
            trainable=True,
            name='batch_normalization_bias'
        )
        self.batch_normalization = self.add_weight(
            shape=(int(input_shape[-1]),),
            initializer='zeros',
            trainable=True,
            name='batch_normalization_weights'
        )
        self._quantization_config = self.quantization_config()

    def train_step(self, data):
        x, y = data
        with tf.GradientTape() as tape:
            x_output = self(x)
            loss = tf.keras.losses.sparse_categorical_crossentropy(y_true=y, y_pred=x_output)
            total_loss = tf.reduce_mean(loss)
        grads = tape.gradient(total_loss, self.trainable_variables)
        self.optimizer.apply_gradients(zip(grads, self.trainable_variables))
        return {"loss": total_loss}

    def call(self, x):
        x_output = tf.keras.layers.BatchNormalization(gamma_initializer="ones")(x) * tf.keras.layers.Activation('relu')(x)
        return x_output * tf.concat((self.kernel * 0.0001, 0.0001), axis=-1)

quantized_model = tf.keras.Sequential([
  QuantizedBatchNormalization(),
  Dense(64, activation='relu'),
  Dense(64, activation='relu'),
  Dense(10, activation='softmax')
])

quantized_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
