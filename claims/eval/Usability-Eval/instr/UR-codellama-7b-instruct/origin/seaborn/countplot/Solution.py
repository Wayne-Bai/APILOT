
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("data.csv")

# Create a bar plot of the counts by category
sns.countplot(x="category", data=df)
plt.show()
