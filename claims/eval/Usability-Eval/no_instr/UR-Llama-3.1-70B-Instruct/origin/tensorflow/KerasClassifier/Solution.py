import tensorflow as tf
from tensorflow import keras
from sklearn.base import BaseEstimator
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

class TensorFlowClassifier(BaseEstimator):
    def __init__(self, epochs=10, batch_size=32, learning_rate=0.001):
        self.epochs = epochs
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.model = None

    def _build_model(self, input_shape, num_classes):
        self.model = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=input_shape),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(num_classes, activation='softmax')
        ])
        self.model.compile(loss='sparse_categorical_crossentropy', 
                            optimizer=keras.optimizers.Adam(learning_rate=self.learning_rate), 
                            metrics=['accuracy'])

    def fit(self, X, y):
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
        self._build_model((X.shape[1],), len(set(y)))
        self.model.fit(X_train, y_train, epochs=self.epochs, batch_size=self.batch_size, 
                        validation_data=(X_val, y_val), verbose=0)

    def predict(self, X):
        return self.model.predict(X).argmax(-1)

    def predict_proba(self, X):
        return self.model.predict(X)

    def score(self, X, y):
        y_pred = self.predict(X)
        return accuracy_score(y, y_pred)

# Example usage:
if __name__ == "__main__":
    from sklearn.datasets import load_iris
    iris = load_iris()
    X = iris.data
    y = iris.target

    tf_clf = TensorFlowClassifier()
    tf_clf.fit(X, y)
    y_pred = tf_clf.predict(X)
    print(classification_report(y, y_pred))
