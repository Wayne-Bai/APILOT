import pandas as pd
import numpy as np
import scipy.stats as stats

# Create a sample DataFrame
np.random.seed(0)
index = pd.date_range('2022-01-01', periods=365, freq='D')
data = np.random.rand(365)
df = pd.DataFrame({'Value': data}, index=index)

# Calculate rolling mean with a window size of 30
rolling_mean_30 = df['Value'].rolling(window=30).mean()

# Calculate rolling standard deviation with a window size of 30
rolling_std_30 = df['Value'].rolling(window=30).std()

# Calculate rolling bias-corrected population standard deviation with a window size of 30
rolling_std_bias_30 = df['Value'].rolling(window=30).apply(stats.tstd)

# Calculate rolling skewness with a window size of 30
rolling_skew_30 = df['Value'].rolling(window=30).apply(stats.skew)

# Calculate rolling kurtosis with a window size of 30
rolling_kurt_30 = df['Value'].rolling(window=30).apply(stats.kurtosis)

# Print the results
print("Rolling Mean 30 Days: ", rolling_mean_30)
print("Rolling Standard Deviation 30 Days: ", rolling_std_30)
print("Rolling Bias-Corrected Population Standard Deviation 30 Days: ", rolling_std_bias_30)
print("Rolling Skewness 30 Days: ", rolling_skew_30)
print("Rolling Kurtosis 30 Days: ", rolling_kurt_30)

