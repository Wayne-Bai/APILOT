
from sklearn.linear_model import ARDRegression

# Create an instance of ARD regression model
model = ARDRegression()

# Fit the model with training data X and Y
model.fit(X, Y)

# Obtain the estimated alpha (precision of the noise distribution)
alpha_ = model.alpha_

# Obtain the estimated lambda (precisions of the weights distribution)
lambda_ = model.lambda_
