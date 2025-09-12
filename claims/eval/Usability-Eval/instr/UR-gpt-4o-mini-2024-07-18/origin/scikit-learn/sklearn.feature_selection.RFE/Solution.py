from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Logistic Regression model
model = LogisticRegression(max_iter=200)

# Create the RFE model and select the top 2 features
rfe = RFE(estimator=model, n_features_to_select=2)
rfe.fit(X_train, y_train)

# Summarize the selected features
selected_features = rfe.support_
ranking = rfe.ranking_

print("Selected Features:", selected_features)
print("Feature Ranking:", ranking)
