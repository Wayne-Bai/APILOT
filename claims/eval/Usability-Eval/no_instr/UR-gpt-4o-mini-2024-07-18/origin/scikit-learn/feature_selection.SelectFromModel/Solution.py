from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

class ImportanceSelector(BaseEstimator, TransformerMixin):
    def __init__(self, model, threshold='mean'):
        self.model = model
        self.threshold = threshold
        self.selector = None

    def fit(self, X, y):
        self.model.fit(X, y)
        self.selector = SelectFromModel(self.model, threshold=self.threshold, prefit=True)
        return self

    def transform(self, X):
        return self.selector.transform(X)

# Example usage
if __name__ == "__main__":
    # Create a synthetic dataset
    X, y = make_classification(n_samples=100, n_features=20, n_informative=10, n_redundant=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the ImportanceSelector with a RandomForest model
    model = RandomForestClassifier(random_state=42)
    selector = ImportanceSelector(model=model)

    # Fit the model and select features
    selector.fit(X_train, y_train)
    X_train_selected = selector.transform(X_train)
    X_test_selected = selector.transform(X_test)

    print(f"Original number of features: {X_train.shape[1]}")
    print(f"Selected number of features: {X_train_selected.shape[1]}")
