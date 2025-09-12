import pandas as pd

def infer_dtypes(df):
    dtypes = {
        "float": 0,
        "object": 0,
        "bool": 0,
        "int": 0,
        "complex": 0
    }

    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            if pd.api.types.is_float_dtype(df[col]):
                dtypes["float"] += 1
            else:
                dtypes["int"] += 1

        if pd.api.types.is_bool_dtype(df[col]):
            dtypes["bool"] += 1

        if pd.api.types.is_complex_dtype(df[col]):
            dtypes["complex"] += 1

        if pd.api.types.is_datetime64_any_dtype(df[col]):
            dtypes["datetime"] = 1

        if pd.api.types.is_timedelta64_dtype(df[col]):
            dtypes["timedelta"] = 1

    return dtypes

df = pd.DataFrame({
    'A': ['1', '2', '3'],
    'B': [1.1, 2.2, 3.3],
    'C': [True, False, True],
    'D': [complex(1, 1), complex(2, 2), complex(3, 3)],
    'E': pd.DatetimeIndex(['2022-01-01', '2022-01-02', '2022-01-03']).to_series(),
    'F': pd.to_timedelta(['1 days', '2 days', '3 days'])
})

dtypes_info = infer_dtypes(df)
print(dtypes_info)
