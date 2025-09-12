# Import necessary libraries
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the iris dataset
digits = load_digits()

# Define a logistic regression classifier
classifier = LogisticRegression()

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
data_scaled = scaler.fit_transform(digits.data)

# Generate a learning curve
train_sizes, train_scores, test_scores = learning_curve(
    classifier, data_scaled, digits.target, cv=5, train_sizes=[0.1, 0.25, 0.5, 0.75, 1.0], n_jobs=-1
)

# Calculate the average score for each train and test size
train_mean = train_scores.mean(axis=1)
test_mean = test_scores.mean(axis=1)

# Plot the learning curve
plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_mean, label='Training Score')
plt.plot(train_sizes, test_mean, label='Cross Validation Score')

# Settings for the plot
plt.xscale('log')
plt.xlabel('Training Example Size')
plt.ylabel('Score')
plt.title('Learning Curve of Logistic Regression for Digits Dataset')
plt.legend()
plt.show()
