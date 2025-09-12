import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'var_1': [1.2, 1.1, 1.4, 2.0],
    'return_1': [0.3, 0.3, 0.1, -0.1]
}
df = pd.DataFrame(data)

# Create points and error bars
sns.barplot(x='var_1', y='return_1', data=df, yerr='var_1', capsize=0.5, ci=None, color="skyblue")

# Show plot
plt.show()
