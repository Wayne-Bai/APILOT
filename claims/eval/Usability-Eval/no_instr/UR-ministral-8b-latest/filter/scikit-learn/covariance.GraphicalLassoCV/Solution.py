import numpy as np
from sklearn.covariance import LedoitWolf
from sklearn.metrics import make_scorer
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import make_covariance

# Generate a random dataset with known covariance
X, _ = make_covariance(n_samples=100, cov=flying_spike())
X = np.random.randn(100, 2)

# Cross-validate Ledoit-Wolf with different l1 penalties
def l1_penalty(n: int):
    lw = LedoitWolf()
    scorer = make_scorer(lw._scorer_)
    param_grid = {'_l1_penalty': np.logspace(-2, 2, num=n)}
    grid_search = GridSearchCV(scorer=scorer, param_grid=param_grid, cv=5)
    grid_search.fit(X)
    return grid_search

for n in [5, 10, 20]:  # Vary the number of penalty values to search over
    print(f'Searching over {n} logarithmically spaced l1 penalties...')
    gs = l1_penalty(n)
    best_params = gs.best_params_
    print(f"Best l1 penalty: {best_params['_l1_penalty']}")
