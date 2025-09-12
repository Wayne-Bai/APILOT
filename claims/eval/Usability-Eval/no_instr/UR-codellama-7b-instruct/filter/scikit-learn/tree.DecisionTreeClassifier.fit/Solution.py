
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# load the dataset
df = pd.read_csv('dataset.csv')

# split the data into training and testing sets
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# build a decision tree classifier from the training set
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
