import pandas as pd
from modules.geocode import loadCachedData
from modules.preprocess import preprocess
from modules.network import buildRegressor
from modules.performance import performance
from modules.mapPlot import createAQIMap

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

# Assuming df has 'AQI Value' (actual) and 'Predicted AQI Value' from model
actual_map = createAQIMap(df, 'AQI Value', title="Actual AQI")
predicted_map = createAQIMap(df, 'Predicted AQI Value', title="Predicted AQI")

# Save maps
actual_map.save('actual_aqi_map.html')
predicted_map.save('predicted_aqi_map.html')
