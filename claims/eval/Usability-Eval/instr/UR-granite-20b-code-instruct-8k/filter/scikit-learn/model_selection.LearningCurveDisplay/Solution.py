from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.linear_model import LogisticRegression

# load iris dataset as an example
iris = datasets.load_iris()
X = iris.data
y = iris.target

# create a base model
base_model = LogisticRegression(random_state=0)

# calculate the learning curve
train_sizes, train_scores, test_scores = learning_curve(
    base_model, X, y, cv=5, n_jobs=-1, scoring='accuracy')

# plot the learning curve
plt.figure()
plt.title("Learning Curve")
plt.xlabel("Training examples")
plt.ylabel("Score")
plt.grid()
plt.plot(train_sizes, train_scores, 'o-', color="r", label="Training score")
plt.plot(train_sizes, test_scores, 'o-', color="g", label="Cross-validation score")
plt.legend(loc="best")
plt.show()
