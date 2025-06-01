import pandas as pd
from modules.geocode import loadCachedData
from modules.preprocess import preprocess
from modules.network import buildRegressor
from modules.performance import performance
from modules.mapPlot import createAQIMap

df = pd.read_csv("data/airQualityData.csv")
df = loadCachedData(df)

df, X, y = preprocess(df)

model = buildRegressor(X, y)

predictions = model.predict(X).flatten() 
df['Predicted AQI Value'] = predictions

performance(df, predictedCol='Predicted AQI Value', trueCol='AQI Value')

actual_map = createAQIMap(df, 'AQI Value', title="Actual AQI")
predicted_map = createAQIMap(df, 'Predicted AQI Value', title="Predicted AQI")

actual_map.save('actual_aqi_map.html')
predicted_map.save('predicted_aqi_map.html')