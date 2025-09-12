# Importing necessary libraries
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import numpy as np

# Meta-transformer for selecting features based on importance weights
class ImportanceSelect(BaseEstimator, TransformerMixin):
    def __init__(self, estimator, threshold=0.1):
        self.estimator = estimator
        self.threshold = threshold

    def fit(self, X, y):
        self.estimator.fit(X, y)
        self.feature.importances_ = self.estimator.feature_importances_
        return self

    @property
    def feature(self):
        if not hasattr(self, 'feature_'):
            self.feature_ = SelectFromModel(self.estimator, threshold=self.threshold)
        return self.feature_

    def transform(self, X):
        return self.feature.transform(X)


# Example usage
if __name__ == "__main__":
    # Generate a random dataset
    X, y = make_classification(n_samples=1000, n_features=50, random_state=42)

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Create a random forest classifier
    rf = RandomForestClassifier(n_estimators=100, random_state=42)

    # Create a meta-transformer
    select = ImportanceSelect(rf)

    # Create a pipeline with the meta-transformer and the classifier
    pipeline = Pipeline([
        ('select', select),
        ('classify', rf)
    ])

    # Train the pipeline
    pipeline.fit(X_train, y_train)

    # Evaluate the pipeline
    score = pipeline.score(X_test, y_test)
    print(f"Accuracy: {score:.3f}")

    # Get the feature importances
    importances = rf.feature_importances_
    print("Feature importances:")
    print(importances)

    # Get the selected features
    selected_features = pipeline.named_steps['select'].feature.get_support()
    print("Selected features:")
    print(selected_features)
