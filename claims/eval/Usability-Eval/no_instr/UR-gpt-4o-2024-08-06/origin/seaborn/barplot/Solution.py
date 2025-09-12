import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate example data
np.random.seed(0)
data = pd.DataFrame({
    "category": np.random.choice(["A", "B", "C"], size=100),
    "value": np.random.normal(loc=10, scale=5, size=100)
})

# Create the bar plot with error bars
sns.barplot(x='category', y='value', data=data, ci="sd", capsize=.2)

# Add titles and labels
plt.title("Bar plot with point estimates and errors")
plt.xlabel("Category")
plt.ylabel("Value")

# Display the plot
plt.show()
