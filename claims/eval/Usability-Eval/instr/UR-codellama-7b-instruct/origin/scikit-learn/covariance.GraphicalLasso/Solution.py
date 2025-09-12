
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

# Load data
corpus = pd.read_csv('data/corpus.csv')

# Preprocess data
scaler = StandardScaler()
tfidf = TfidfVectorizer(stop_words='english', max_df=0.5)
X = tfidf.fit_transform(corpus['text'])
y = scaler.fit_transform(corpus['rating']).ravel()

# Create Lasso regularized LinearRegression model
model = LinearRegression(n_jobs=-1)
l1_reg = 0.1
model.set_params(penalty='l1', alpha=l1_reg, fit_intercept=False)

# Fit model to data
model.fit(X, y)

# Get sparse inverse covariance matrix
cov_mat = model.covariance_
