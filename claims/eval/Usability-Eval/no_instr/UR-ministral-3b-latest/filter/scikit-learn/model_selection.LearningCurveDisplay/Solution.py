from sklearn.model_selection import learning_curve
import numpy as np
import matplotlib.pyplot as plt

X, y = ...  # Assume you have your dataset here
titles = ['Training', 'Validation', 'Size of the dataset']

for i in range(len(titles)):
    train_sizes, train_scores, val_scores = learning_curve(estimator = DecisionTreeClassifier(), # Adjust this to your estimator
                                                            X = X,
                                                            y = y,
                                                            cv = 5,
                                                            scoring = 'accuracy',
                                                            n_jobs = -1)
    train_scores_mean = np.mean(train_scores, axis=1)
    val_scores_mean = np.mean(val_scores, axis=1)

    plt.figure()
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, val_scores_mean, 'o-', color="g",
             label="Cross-validation score")

    plt.title(titles[i])
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    plt.legend(loc="best")

plt.show()
