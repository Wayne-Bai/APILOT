import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

class TensorFlowClassifier(KerasClassifier):
    def __init__(self, num_neurons=10, num_epochs=100, batch_size=32, verbose=1):
        super(TensorFlowClassifier, self).__init__(
            model=Sequential(),
            num_neurons=num_neurons,
            num_epochs=num_epochs,
            batch_size=batch_size,
            verbose=verbose
        )

    def fit(self, x, y, **kwargs):
        x = x.astype('float32')
        y = y.astype('int32')
        x = StandardScaler().fit_transform(x)
        return super(TensorFlowClassifier, self).fit(x, y, **kwargs)

    def predict(self, x):
        x = x.astype('float32')
        x = StandardScaler().transform(x)
        return super(TensorFlowClassifier, self).predict(x)
