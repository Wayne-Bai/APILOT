
from sklearn import linear_model

# Assuming you have already prepared your training data and target variable
# X_train and y_train

# Create a linear regression model
model = linear_model.LinearRegression()

# Train the model using the training data
model.fit(X_train, y_train)
