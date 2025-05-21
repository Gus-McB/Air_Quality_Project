import pandas as pd
from modules.geocode import geocodeLocations, loadCachedData
from modules.preprocess import preprocess
from modules.network import buildClassifier
from modules.performance import performance  

df = pd.read_csv(r"data\airQualityData.csv")
df = loadCachedData(df)

df, X, y = preprocess(df)

model, label_encoder = buildClassifier(X, y)

y_pred_prob = model.predict(X)
y_pred = label_encoder.inverse_transform(y_pred_prob.argmax(axis=1))

df['PredictedAQICategory'] = y_pred
performance(df, predictedCol='PredictedAQICategory', trueCol='AQI Category')
