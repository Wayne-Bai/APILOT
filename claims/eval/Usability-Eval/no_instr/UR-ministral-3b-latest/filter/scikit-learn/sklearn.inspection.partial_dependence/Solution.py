from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold
from sklearn.datasets import load_breast_cancer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load dataset
data = load_breast_cancer()

#Get all features except target
X = pd.DataFrame(data.data, columns= data.feature_names)
y = data.target

#split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Fit the Random Forest model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

#partial dependence
feature = ["mean radius"]
kf = KFold(n_splits=10)

larger_grid = np.linspace(X_train[feature[0]].min(), X_train[feature[0]].max(), 100)
partial_dependence_dict = {}

for i in range(100):
    partial_dependence_dict[larger_grid[i]] = []

for train_index, test_index in kf.split(X_train):
    X_train_fold, X_test_fold = X_train.loc[train_index], X_train.loc[test_index]
    X_test_fold.loc[i, feature[0]] = larger_grid[i]

    y_test_fold = y_test.loc[test_index[i]]

    clf_fold = clf.fit(X_train_fold, y_test_fold)
    pd = clf_predict_function(clf_fold, X_test_fold, Y_test_fold)
    partial_dependence_dict[larger_grid[i]].append(pd.predict_proba(X_test_fold)[:,1])

partial_dependence_df = pd.DataFrame.from_dict(partial_dependence_dict)
plt.plot(partial_dependence_df.index, partial_dependence_df.T)
plt.xlabel('Value of feature x')
plt.ylabel('Partial Dependence coefficients for each fold')
plt.show()
