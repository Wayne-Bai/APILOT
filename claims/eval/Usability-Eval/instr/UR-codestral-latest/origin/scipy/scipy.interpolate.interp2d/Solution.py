import numpy as np
from scipy.interpolate import griddata

# create some data
x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

# interpolate
xnew = np.linspace(0, 1, 200)
ynew = np.linspace(0, 1, 200)
Xnew, Ynew = np.meshgrid(xnew, ynew)
Znew = griddata((X.ravel(), Y.ravel()), Z.ravel(), (Xnew, Ynew), method='cubic')
