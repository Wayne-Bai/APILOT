
import pandas as pd

# Create a DatetimeIndex with a frequency of '5Min' from the current time
df = pd.date_range(start=pd.Timestamp.now(), freq='5Min', closed='left')
