
import seaborn as sns
import matplotlib.pyplot as plt

# Create a dataset of random observations
x = np.linspace(0, 10, 100)
y = np.random.normal(size=100) + x**2

# Draw a patch representing a KDE
sns.kdeplot(x, y, shade=True)
plt.show()
