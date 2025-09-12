from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split

# Assuming you have your data and labels stored in X and y
# Splitting the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Creating a Naive Bayes classifier for multivariate Bernoulli models
clf = BernoulliNB()

# Training the model using the training sets
clf.fit(X_train, y_train)

# Predicting the response for test dataset
y_pred = clf.predict(X_test)
