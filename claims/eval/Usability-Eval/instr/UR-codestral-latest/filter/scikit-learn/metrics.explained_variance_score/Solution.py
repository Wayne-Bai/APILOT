# Importing required libraries
from sklearn.metrics import explained_variance_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Assuming we have a dataset in X_data and y_data
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state=42)

# We will use a simple linear regression model as an example
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = model.predict(X_test)

# Calculate the explained variance regression score
explained_variance = explained_variance_score(y_test, y_pred)

print('Explained Variance Regression Score: ', explained_variance)
