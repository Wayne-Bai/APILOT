from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score

# Generate a multivariate Bernoulli dataset
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=20,
    n_redundant=0,
    random_state=42,
    n_clusters_per_class=1,
    weights=None,
    flip_y=0,
    class_sep=1.0,
    data_type='binary')

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Bernoulli Naive Bayes model
bn = BernoulliNB()
bn.fit(X_train, y_train)

# Predict the test set results
y_pred = bn.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of Bernoulli Naive Bayes classifier: {accuracy}")
