import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data for demonstration
data = {
    'color': ['red', 'red', 'blue', 'blue', 'green', 'red', 'blue', 'blue', 'green', 'green']
}

df = pd.DataFrame(data)

# Plot the counts of observations in each categorical bin using bars
sns.countplot(x='color', data=df)
plt.title('Counts of Observations in Each Categorical Bin')
plt.show()
