import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# Generate a random dataset
X, y = make_classification(n_samples=1000, n_features=4, n_informative=2, n_redundant=0, random_state=42)

# Create a random forest classifier
clf = RandomForestClassifier(random_state=42)

# Generate the learning curve
train_sizes, train_scores, test_scores = learning_curve(clf, X, y, cv=5, scoring='accuracy', n_jobs=1, train_sizes=np.linspace(0.1, 1.0, 5))

# Calculate the mean and standard deviation of the training and test scores
train_scores_mean = -train_scores.mean(axis=1)
train_scores_std = -train_scores.std(axis=1)
test_scores_mean = -test_scores.mean(axis=1)
test_scores_std = -test_scores.std(axis=1)

# Plot the learning curve
plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.1, color='r')
plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.1, color='g')
plt.plot(train_sizes, train_scores_mean, 'o-', color='r', label='Training score')
plt.plot(train_sizes, test_scores_mean, 'o-', color='g', label='Cross-validation score')
plt.xlabel('Training examples')
plt.ylabel('Score')
plt.title('Learning curve for random forest classifier')
plt.legend(loc='best')
plt.show()
