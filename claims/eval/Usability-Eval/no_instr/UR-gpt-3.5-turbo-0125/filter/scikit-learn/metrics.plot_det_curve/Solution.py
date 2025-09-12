
import matplotlib.pyplot as plt
from sklearn.metrics import plot_roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Insert code to load or define your dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)

plot_roc_curve(classifier, X_test, y_test)
plt.show()
