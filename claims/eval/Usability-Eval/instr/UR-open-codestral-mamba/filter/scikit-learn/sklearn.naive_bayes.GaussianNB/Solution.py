from sklearn.naive_bayes import GaussianNB

# initialize the GaussianNB model
model = GaussianNB()

# define function to make predictions
def predict(features):
    prediction = model.predict(features)
    return prediction

# define function to update model parameters
def train(features, labels):
    model.partial_fit(features, labels, classes=np.unique(labels))
    return 'Model trained successfully'
