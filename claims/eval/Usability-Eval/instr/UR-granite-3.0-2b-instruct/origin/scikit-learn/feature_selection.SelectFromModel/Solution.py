from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import numpy as np

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Create a Logistic Regression model
model = LogisticRegression()

# Fit the model on the training set
model.fit(X_train, y_train)

# Use SelectKBest with f_classif to select top 2 features
selector = SelectKBest(score_func=f_classif, k=2)
X_train_selected = selector.fit_transform(X_train, y_train)
X_test_selected = selector.transform(X_test)

# Print the selected features
print("Selected features: ", np.where(selector.get_support())[0])

# Print the accuracy of the model with selected features
print("Accuracy with selected features: ", model.score(X_test_selected, y_test))
