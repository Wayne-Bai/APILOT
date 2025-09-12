import pandas as pd
import matplotlib.pyplot as plt

# Let's say we have a dataframe 'df'
df = pd.DataFrame({
   'apples': [30, 25, 40, 15],
   'oranges': [25, 30, 45, 10]
}, index=['2017 Sales', '2018 Sales', '2019 Sales', '2020 Sales'])

df.plot(kind='bar', stacked=True, figsize=(10, 5), color=['lightblue','lightcoral'])
plt.xlabel("Years")
plt.ylabel("Fruit sold in millions")
plt.title("Fruit Sales by Year")
plt.show()
