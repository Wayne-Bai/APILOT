
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

# load the boston housing prices dataset
boston = datasets.load_boston()

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2, random_state=42)

# return the loaded boston dataset
return boston
