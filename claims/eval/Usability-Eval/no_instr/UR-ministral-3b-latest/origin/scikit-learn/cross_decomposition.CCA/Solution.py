from sklearn.cross_decomposition import CanonicalCorrelation

# Train the Canonical Correlation Analysis model
ccu = CanonicalCorrelation()
y = ccu.fit(X1, X2)
y.linearitas_noist_data
