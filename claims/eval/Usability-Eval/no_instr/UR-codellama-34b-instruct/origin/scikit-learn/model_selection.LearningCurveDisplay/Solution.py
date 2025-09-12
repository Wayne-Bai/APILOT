
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt

# Create a dataset and train/test split
X, y = make_classification(n_samples=1000, n_features=20, n_informative=5, n_redundant=5)
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a learning curve plot
train_sizes, train_scores, test_scores = learning_curve(train_x, train_y, test_x, test_y, cv=5, scoring='accuracy')
plt.plot(train_sizes, train_scores)
plt.plot(train_sizes, test_scores)
plt.legend(['Training Score', 'Testing Score'])
plt.show()
