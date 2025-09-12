
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# generate some example data
np.random.seed(0)
n_samples = 50
data = np.random.randint(1, 100, n_samples).reshape(-1, 1)
data_dict = {"value": data}

# draw a strip plot with jitter to reduce overplotting
sns.stripplot(x="value", y=data, jitter=True)
plt.show()
