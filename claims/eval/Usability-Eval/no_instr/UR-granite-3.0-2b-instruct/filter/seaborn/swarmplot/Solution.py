import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")

# Create a categorical scatterplot with points adjusted to be non-overlapping
# We will use the 'jointplot' function and set 'orient' to 'h' for horizontal plot
# Then, we will remove the overlapping points by setting 'scatter_kws' to a dictionary
# with 'alpha' set to a low value (e.g., 0.5) to make the points semi-transparent
sns.jointplot(x="total_bill", y="tip", data=tips, kind="hist", stat="density",
             hue="sex", color="black", ci=None, marginal_kws=dict(alpha=0.5),
             scatter_kws=dict(alpha=0.5))

# Show the plot
plt.show()
