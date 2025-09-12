import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the example dataset
data = load_iris()
X, y = data.data, data.target

# Split the data into a training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestClassifier(random_state=42)

def recursive_feature_elimination_ranking(estimator, X, y):
    """
    Perform feature ranking with recursive feature elimination
    
    Parameters:
    estimator: a fitted model with attribute 'feature_importances_'
    X: array-like, shape (n_samples, n_features)
    y: array-like, shape (n_samples,)

    Returns:
    rankings: array, shape (n_features,)
        Feature ranking - higher rank means more important feature.
    """
    model.fit(X, y)
    importances = model.feature_importances_
    
    # Sort features based on their importance scores, higher is better
    rankings = np.argsort(importances)[::-1]
    return rankings

# Perform recursive feature elimination feature ranking
rankings = recursive_feature_elimination_ranking(model, X_train, y_train)

# Print the rankings
print("Feature ranking:")
for i, rank in enumerate(rankings):
    print(f"Feature {i + 1}: {data.feature_names[rank]} (Rank: {i + 1}, Importance: {model.feature_importances_[rank]:.4f})")
