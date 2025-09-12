# Importing necessary libraries
from sklearn.naive_bayes import BernoulliNB
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Creating a multivariate Bernoulli dataset
X, y = make_classification(n_samples=1000, 
                           n_features=10, 
                           n_informative=5, 
                           n_redundant=3, 
                           random_state=1,
                           n_clusters_per_class=1)

# Splitting the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating a Naive Bayes classifier for multivariate Bernoulli models
bnb = BernoulliNB()

# Training the model using the training sets
bnb.fit(X_train, y_train)

# Predicting the response for the test dataset
y_pred = bnb.predict(X_test)

# Model Accuracy: how often is the classifier correct?
print("Accuracy:", accuracy_score(y_test, y_pred))

# Precision and recall, F1 score
print("Classification Report:")
print(classification_report(y_test, y_pred))
