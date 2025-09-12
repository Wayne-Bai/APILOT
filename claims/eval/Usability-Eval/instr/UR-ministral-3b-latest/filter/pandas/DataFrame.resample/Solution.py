
import pandas as pd

# create a sample time series data from 2010-01-01 to 2010-12-31 with values from 1 to 365:
data = {'date': pd.date_range(start='2010-01-01', periods=365), 'value': range(365)}
readable_data = pd.DataFrame(data)
readable_data
