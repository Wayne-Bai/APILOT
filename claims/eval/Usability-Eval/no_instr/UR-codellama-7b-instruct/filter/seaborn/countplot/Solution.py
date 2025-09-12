
import seaborn as sns
import matplotlib.pyplot as plt

# load the data
tips = sns.load_dataset('tips')

# create a count plot of the number of observations in each categorical bin
sns.countplot(x='day', data=tips)

# add a title to the plot
plt.title("Count of Observations by Day")

# show the plot
plt.show()
