from sklearn import datasets
from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import train_test_split

# Load the Boston Housing dataset
boston = datasets.load_boston()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2, random_state=42)

# Initialize the Bayesian Ridge model
model = BayesianRidge()

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict the target variable for the test set
y_pred = model.predict(X_test)
