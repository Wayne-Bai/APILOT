import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

class MetaTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, model=RandomForestClassifier(n_estimators=100)):
        self.model = model
        self.selector = SelectFromModel(self.model)

    def fit(self, X, y=None):
        self.selector.fit(X, y)
        return self

    def transform(self, X):
        return self.selector.transform(X)

# Example usage
if __name__ == "__main__":
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.svm import SVC

    # Load dataset
    data = load_iris()
    X, y = data.data, data.target

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Create pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('feature_selection', MetaTransformer()),
        ('classifier', SVC())
    ])

    # Fit the pipeline
    pipeline.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = pipeline.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
