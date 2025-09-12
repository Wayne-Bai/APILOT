from sklearn.datasets import load_iris
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# Load dataset
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a logistic regression model
model = LogisticRegression(max_iter=1000)

# Create RFE model and select the top 2 features
rfe = RFE(estimator=model, n_features_to_select=2)
rfe.fit(X_train, y_train)

# Summarize selected features
selected_features = X.columns[rfe.support_]
print("Selected Features:", selected_features.tolist())
