import numpy as np
from sklearn import datasets
from sklearn.linear_model import LarsIC

# Load sample data
X, y = datasets.load_diabetes(return_X_y=True)

# Initialize and fit the LassoLarsIC model using BIC for model selection
model_bic = LarsIC(criterion='bic')
model_bic.fit(X, y)

# Alternatively, use AIC for model selection
model_aic = LarsIC(criterion='aic')
model_aic.fit(X, y)

# Output results
print("Lasso model with LARS using BIC selected alpha:", model_bic.alpha_)
print("Lasso model with LARS using AIC selected alpha:", model_aic.alpha_)

# Optionally, you can plot the resulting IC scores
import matplotlib.pyplot as plt

def plot_ic(model, title):
    alphas = -np.log10(model.alphas_)
    plt.figure()
    plt.plot(alphas, model.criterion_, label='Information Criterion')
    plt.axvline(-np.log10(model.alpha_), linestyle='--', color='k', label='Best alpha')
    plt.xlabel('-log10(alpha)')
    plt.ylabel('criterion')
    plt.title(title)
    plt.legend()
    plt.show()

plot_ic(model_bic, 'Model Selection using BIC')
plot_ic(model_aic, 'Model Selection using AIC')
