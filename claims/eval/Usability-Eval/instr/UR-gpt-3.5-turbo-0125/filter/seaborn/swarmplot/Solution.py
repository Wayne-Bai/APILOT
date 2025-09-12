
import seaborn as sns
import matplotlib.pyplot as plt

# Generate some example data
tips = sns.load_dataset("tips")

# Adjust the x and y coordinates for non-overlapping points
def jitter(x, jitter_amount=0.2):
    return x + jitter_amount * (2 * np.random.rand(len(x)) - 1)

# Create the categorical scatterplot with non-overlapping points
sns.stripplot(x=jitter(tips["day"]), y=jitter(tips["total_bill"]))

plt.show()
