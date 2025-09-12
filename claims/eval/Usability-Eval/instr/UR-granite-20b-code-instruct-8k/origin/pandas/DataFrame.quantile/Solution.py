import pandas as pd
def return_values_at_quantile(data, quantile):
    return data.quantile(quantile)
