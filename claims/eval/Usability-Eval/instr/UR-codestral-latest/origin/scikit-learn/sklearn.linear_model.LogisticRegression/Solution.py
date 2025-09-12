from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# assume that we have X and y as our features and target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create an instance of the logistic regression model
lr_model = LogisticRegression(max_iter=1000)

# fit the model with the training data
lr_model.fit(X_train, y_train)

# predict the target on the test data
y_pred = lr_model.predict(X_test)

# print classification report
print(classification_report(y_test, y_pred))
