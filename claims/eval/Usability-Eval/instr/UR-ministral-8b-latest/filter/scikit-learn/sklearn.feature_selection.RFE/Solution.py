import numpy as np
import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.svm import SVC

# Load dataset
data = pd.read_csv('your_dataset.csv')
X = data.drop('target', axis=1)
y = data['target']

# Initialize the model for RFE
model = SVC()

# Initialize RFE with the model
rfe = RFE(model, n_features_to_select=5)  # Replace with your desired number of features to select

# Fit RFE to the data
rfe.fit(X, y)

# Get selected features
selected_features = X.columns[rfe.support_]
print("Selected features: ", selected_features)
