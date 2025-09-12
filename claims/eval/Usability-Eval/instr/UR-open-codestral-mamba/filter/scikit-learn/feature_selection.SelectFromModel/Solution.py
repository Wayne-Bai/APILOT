# Importing libraries from scikit-learn
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Creating meta-transformer
class ImportanceBasedFeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, model):
        self.model = model

    def fit(self, X, y):
        self.model.fit(X, y)
        if hasattr(self.model, "feature_importances_"):
            self.importance_scores = self.model.feature_importances_
        else:
            self.importance_scores = self.model.coef_[0]

    def transform(self, X):
        if self.importance_scores is None:
            raise ValueError("Model must be trained first")
        sorted_idx = self.importance_scores.argsort()
        sorted_importance = self.importance_scores[sorted_idx]
        selected_features = sorted_idx[sorted_importance > 0]
        return X[:, selected_features]

# Use the ImportanceBasedFeatureSelector in a pipeline with a classifier
model = RandomForestClassifier()
transformer = ImportanceBasedFeatureSelector(model)

# Assume X_train and y_train are available
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
transformer.fit(X_train_scaled, y_train)
X_train_reduced = transformer.transform(X_train_scaled)
