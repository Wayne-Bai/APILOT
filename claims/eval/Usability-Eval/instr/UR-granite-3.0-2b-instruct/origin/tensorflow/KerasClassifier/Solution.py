import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier

class TensorFlowClassifier(KerasClassifier):
    def __init__(self, hidden_layers=(64,64), output_units=1, activation='relu', optimizer='adam', loss='mse', metrics=['accuracy']):
        super().__init__(builder=self.build_model, input_shape=(None, 1), output_units=output_units, hidden_layers=hidden_layers, activation=activation, optimizer=optimizer, loss=loss, metrics=metrics)

    def build_model(self, hidden_layers):
        model = Sequential()
        for layer in hidden_layers:
            model.add(Dense(units=layer, activation=self.activation))
        model.add(Dense(units=1, activation='sigmoid'))
        model.compile(optimizer=self.optimizer, loss=self.loss, metrics=self.metrics)
        return model
