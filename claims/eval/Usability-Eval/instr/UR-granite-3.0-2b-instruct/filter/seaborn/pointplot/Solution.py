import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df is your DataFrame and 'x' and 'y' are your columns
sns.lineplot(data=df, x='x', y='y', ci=95)
plt.show()
