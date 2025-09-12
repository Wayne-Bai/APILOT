from sklearn.feature_selection import SelectFromModel
import pickle

# Load the pre-trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Select features based on model's feature importance
selector = SelectFromModel(model, threshold=0.1, prefit=True)
X_new = selector.transform(X)
