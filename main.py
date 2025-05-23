import pandas as pd
from modules.geocode import loadCachedData
from modules.preprocess import preprocess
from modules.network import buildRegressor
from modules.performance import performance  # Make sure this version is regression-compatible

# Load data
df = pd.read_csv("data/airQualityData.csv")
df = loadCachedData(df)

# Preprocess
df, X, y = preprocess(df)

# Train regression model
model = buildRegressor(X, y)

# Predict AQI values
predictions = model.predict(X).flatten()  # Flatten to 1D if necessary
df['Predicted AQI Value'] = predictions

# Evaluate performance
performance(df, predictedCol='Predicted AQI Value', trueCol='AQI Value')
