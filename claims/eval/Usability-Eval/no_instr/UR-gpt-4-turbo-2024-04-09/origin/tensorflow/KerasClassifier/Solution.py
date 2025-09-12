import tensorflow as tf
from sklearn.base import ClassifierMixin
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier

class TensorFlowKerasClassifier(ClassifierMixin, KerasClassifier):
    def __init__(self, build_fn=None, **kwargs):
        super().__init__(build_fn=build_fn, **kwargs)
        
    def fit(self, x, y, **kwargs):
        return super().fit(x, y, **kwargs)
    
    def predict(self, x):
        return super().predict(x)
    
    def score(self, x, y, **kwargs):
        y_pred = self.predict(x)
        return sum(y_pred == y) / len(y)
    
# Example usage:
def create_model():
    model = Sequential([
        Dense(10, activation='relu', input_shape=(4,)),  # Adjust input_shape based on your feature size
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

tf_clf = TensorFlowKerasClassifier(build_fn=create_model, epochs=10, batch_size=32, verbose=1)
