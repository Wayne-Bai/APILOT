
import tensorflow as tf

class TensorFlowRegressor:
    def __init__(self, model):
        self.model = model
    
    def fit(self, X, y):
        self.model.compile(optimizer='adam', loss='mean_squared_error')
        self.model.fit(X, y, epochs=100, verbose=0)
    
    def predict(self, X):
        return self.model.predict(X)
