from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

class MetaTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.pca = PCA()

    def fit(self, X, y=None):
        self.pca.fit(X)
        return self

    def transform(self, X):
        return X.dot(self.pca.components_.T)

    def fit_transform(self, X, y=None):
        return self.fit(X).transform(X)

# Sample usage
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

meta_transformer = MetaTransformer()
X_train_transformed = meta_transformer.fit_transform(X_train)
X_test_transformed = meta_transformer.transform(X_test)
print("Transformed X_train shape:", X_train_transformed.shape)
print("Transformed X_test shape:", X_test_transformed.shape)
