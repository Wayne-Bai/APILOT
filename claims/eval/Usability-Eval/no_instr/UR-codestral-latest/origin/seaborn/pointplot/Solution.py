import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
fmri = sns.load_dataset("fmri")

# Use lineplot to show point estimates and errors
sns.lineplot(x="timepoint", y="signal", hue="region", style="event", data=fmri, markers=True)

# Show the plot
plt.show()
