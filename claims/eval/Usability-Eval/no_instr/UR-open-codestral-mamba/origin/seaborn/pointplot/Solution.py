import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Assume we have some data
np.random.seed(sum(map(ord, "distributions")))
data = np.random.normal(size=1000)

# Create a distribution plot with point estimates
sns.displot(data, kind="line", stat="count", common_norm=False)

plt.show()
