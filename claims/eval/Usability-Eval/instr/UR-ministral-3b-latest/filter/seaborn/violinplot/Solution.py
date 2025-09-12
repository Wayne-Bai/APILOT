import seaborn as sns

# Create a sample array with some observations
observations = [1, 2, 2, 3, 3, 5, 5, 5, 7, 7, 7, 8]

# Create a plot
sns.kdeplot(observations, stat="density")
