from sklearn.preprocessing import FunctionTransformer

def inverse_transformation(X):
    # define the inverse transformation function
    # e.g., assume the transformation was a simple scaling by 2
    inverse_X = X / 2
    return inverse_X

# create a FunctionTransformer object with the inverse_transformation function
inverse_transformer = FunctionTransformer(inverse_transformation)

# use the inverse_transformer to transform a vector
n_features = 10
X = np.random.rand(n_features)  # example input vector
transformed_X = inverse_transformer.transform(X)

print(transformed_X)
