from sklearn.impute import SimpleImputer

# defining the strategy
imputer = SimpleImputer(strategy='mean')  # using mean strategy

# fit the imputer on the dataset
imputer.fit(df)

# transform the dataset by imputing missing values
df_imputed = imputer.transform(df)
